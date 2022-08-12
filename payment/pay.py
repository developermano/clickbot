import sys
from faucetpay import faucetpay


sys.path.append("./dbfolder")
from mysqlfunc import mysqldb
faucet=faucetpay()

class payuser:
    def sendreward(campaignid,userid):
        get_user_email=mysqldb().get_user_Wallet(userid)
        ref=mysqldb().get_user_ref(userid)
        get_user_referral=mysqldb().get_user_Wallet(ref)
        info=mysqldb().campaignid_to_info(campaignid)
        cpc=info[5]
        adbudget=info[6]
        if adbudget-cpc>0 and not mysqldb().is_completed_already(userid,campaignid):
            mysqldb().add_ad_completion(userid,campaignid)
            total_reward=cpc*100000000
            mysqldb().decrease_ad_budget(campaignid)
            user_reward=faucet.send_trx_to_user(get_user_email,total_reward/2)
            aff_reward=faucet.send_trx_to_user(get_user_referral,total_reward/10)
            mysqldb().add_transaction(userid,campaignid,0,total_reward/2,user_reward['payout_id'])
            mysqldb().add_transaction(ref,userid,1,total_reward/10,aff_reward['payout_id'])
            return True
        else:
            return False
