import sqlite3
import time


while True:
    islemSecim = int(input("New Date:1 Oldest datas:2 Clean All Data:3  "))
    con = sqlite3.connect("bakim.db")
    cursor = con.cursor()

    def veritabaniOlistur():
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS bakim(degistirme_GUN TEXT,degistirme_AY TEXT,degistirme_YIL TEXT)"
        )
        con.commit()

    veritabaniOlistur()

    def veritabaniYazma(gun, ay, yil):
        cursor.execute("INSERT INTO bakim VALUES(?,?,?)", (gun, ay, yil))
        con.commit()

    def veritabaniVericekme():
        cursor.execute("SELECT * FROM bakim")
        date_list = cursor.fetchall()
        for i in date_list:
            print(i)
            time.sleep(1)

    # def cleanData(silGun, silAy, silYil):
    #     cursor.execute(
    #         "DELETE FROM bakim where degistirme_GUN=?,AY=?,YIL=? ",
    #         (silGun, silAy, silYil),
    #     )
    #     con.commit()

    if islemSecim == 1:
        gun_girme = input("Gün Girin:")
        ay_girme = input("Ay Girin:")
        yıl_girme = input("Yıl Girin:")
        veritabaniYazma(gun_girme, ay_girme, yıl_girme)
        print("Ana menüye yönlendiriliyorsunuz.")
        time.sleep(3)

    elif islemSecim == 2:
        veritabaniVericekme()
        print("Ana menüye yönlendiriliyorsunuz..")
        time.sleep(3)
    # elif islemSecim == 3:
    #     veritabaniVericekme()
    #     gun_girme = input("Gün Girin:")
    #     ay_girme = input("Ay Girin:")
    #     yıl_girme = input("Yıl Girin:")
    #     cleanData(gun_girme, ay_girme, yıl_girme)
