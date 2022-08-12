import mysql.connector


class mysqldb:
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(host="localhost", user="phproot", password="root", database="clickbot")
        self.mycursor = self.mydb.cursor()
    

    def insert_user(self, userid, walletaddress, ref):
        sql = "INSERT INTO `user` (`userid`, `walletaddress`, `ref`) VALUES (%s, %s,%s);"
        self.mycursor.execute(sql, (userid, walletaddress, ref))
        self.mydb.commit()

    def isexist_user(self, userid):
        sql = "SELECT * FROM `user` WHERE userid=%s;"
        self.mycursor.execute(sql, (userid,))
        myresult = self.mycursor.fetchall()
        return len(myresult) != 0

    def is_set_wallet(self, userid):
        sql = "SELECT * FROM `user` WHERE userid=%s;"
        self.mycursor.execute(sql, (userid,))
        myresult = self.mycursor.fetchall()
        return myresult[0][1] != '0'

    def update_user_walletaddress(self, userid, walletaddress):
        sql = "UPDATE `user` SET `walletaddress` = %s WHERE userid = %s;"
        self.mycursor.execute(sql, (walletaddress, userid))
        self.mydb.commit()


    def list_my_ads(self, ownerid):
        sql = "SELECT * FROM `ad` WHERE ownerid=%s;"
        self.mycursor.execute(sql, (ownerid,))
        myresult = self.mycursor.fetchall()
        return myresult

    def list_ad_to_user(self,userid,adtype):
        sql = "SELECT * FROM `ad` WHERE totalbudget>cpc AND adtype=%s;"
        self.mycursor.execute(sql, (adtype,))
        myresult = self.mycursor.fetchall()
        for i in myresult:
            sql1="SELECT * FROM `completion` WHERE userid=%s AND campaignid=%s;"
            self.mycursor.execute(sql1, (userid,i[0]))
            myresult1 = self.mycursor.fetchall()
            if len(myresult1)==0:
                return i


    def add_ad_completion(self, userid, campaignid):
        sql = "INSERT INTO `completion` (`userid`, `campaignid`) VALUES (%s,%s);"
        self.mycursor.execute(sql, (userid, campaignid))
        self.mydb.commit()

    def is_completed_already(self, userid,campaignid):
        sql="SELECT * FROM `completion` WHERE userid=%s AND campaignid=%s;"
        self.mycursor.execute(sql, (userid,campaignid))
        myresult = self.mycursor.fetchall()
        return len(myresult)!=0
    
    def campaignid_to_info(self,id):
        sql="SELECT * FROM `ad` WHERE campaignid=%s;"
        self.mycursor.execute(sql, (id,))
        myresult = self.mycursor.fetchall()
        return myresult[0]

    def add_shortner(self, k, v):
        sql="SELECT * FROM `shortenlink` WHERE k=%s;"
        self.mycursor.execute(sql, (k,))
        myresult = self.mycursor.fetchall()
        if len(myresult)==0:
            sql = "INSERT INTO `shortenlink` (`k`, `v`) VALUES (%s,%s);"
            self.mycursor.execute(sql, (k, v))
            self.mydb.commit()

        else:
            sql = "UPDATE `shortenlink` SET k=%s, v=%s WHERE k=%s;"
            self.mycursor.execute(sql, (k, v,k))
            self.mydb.commit()


    def get_shortner(self,k):
        sql="SELECT * FROM `shortenlink` WHERE k=%s;"
        self.mycursor.execute(sql, (k,))
        myresult = self.mycursor.fetchall()
        return myresult[0][1]

    def get_user_Wallet(self,userid):
        sql="SELECT * FROM `user` WHERE userid=%s;"
        self.mycursor.execute(sql, (userid,))
        myresult = self.mycursor.fetchall()
        return myresult[0][1]

    def decrease_ad_budget(self,campaignid):
        sql="SELECT * FROM `ad` WHERE campaignid=%s;"
        self.mycursor.execute(sql, (campaignid,))
        myresult = self.mycursor.fetchall()
        cpc=float(myresult[0][5])
        budget=float(myresult[0][6])
        current_budget=budget-cpc
        sql="UPDATE ad SET totalbudget=%s  WHERE campaignid=%s;"
        self.mycursor.execute(sql, (current_budget,campaignid))
        self.mydb.commit()
        myresult = self.mycursor.fetchall()
        return myresult

    def get_user_ref(self,userid):
        sql="SELECT * FROM `user` WHERE userid=%s;"
        self.mycursor.execute(sql, (userid,))
        myresult = self.mycursor.fetchall()
        return myresult[0][2]
    
    def add_transaction(self, userid, campaignid,campaigntypeindex,balance,payouthash):
        '''campaigntype index : 0-user_reward,1-user_affiliate,2-deposit_affiliate,3-bonus'''
        campaigntype=['user_reward','user_affiliate','deposit_affiliate','bonus']
        sql = "INSERT INTO `transaction` (`userid`, `campaignid`, `type`, `balance`,`payout_hash`) VALUES (%s,%s,%s,%s,%s);;"
        self.mycursor.execute(sql, (userid, campaignid,campaigntype[campaigntypeindex],balance,payouthash))
        self.mydb.commit()

    def createad(self,adtype,ownerid,adurl,extraurl=""):
        sql = "INSERT INTO `ad` (`adtype`, `ownerid`,`adurl`,`extraurl`) VALUES (%s,%s,%s,%s);;"
        self.mycursor.execute(sql, (adtype,ownerid,adurl,extraurl))
        self.mydb.commit()
    
    def update_ad_title(self,campaignid,adtitle):
        sql = "UPDATE `ad` SET `adtitle` = %s WHERE campaignid = %s;"
        self.mycursor.execute(sql, (adtitle, campaignid))
        self.mydb.commit()

    def update_ad_desc(self,campaignid,addesc):
        sql = "UPDATE `ad` SET `adesc` = %s WHERE campaignid = %s;"
        self.mycursor.execute(sql, (addesc, campaignid))
        self.mydb.commit()

    def update_ad_url(self,campaignid,adurl):
        sql = "UPDATE `ad` SET `adurl` = %s WHERE campaignid = %s;"
        self.mycursor.execute(sql, (adurl, campaignid))
        self.mydb.commit()

    def update_ad_cpc(self,campaignid,adcpc):
        sql = "UPDATE `ad` SET `cpc` = %s WHERE campaignid = %s;"
        self.mycursor.execute(sql, (adcpc, campaignid))
        self.mydb.commit()

    def update_extra_url(self,campaignid,adextraurl):
        sql = "UPDATE `ad` SET `extraurl` = %s WHERE campaignid = %s;"
        self.mycursor.execute(sql, (adextraurl, campaignid))
        self.mydb.commit()
