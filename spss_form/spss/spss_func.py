import pandas as pd
import numpy as np
import pyreadstat


def write_spss_data(liste):
    df = pd.read_spss("C:/Users/m-dur/OneDrive/Masaüstü/seminer.sav")
    columns = ['cinsiyetiniz','yaşınız','medenidurum','mezuniyet','yaşadığınyer','bölge','mesleğiseçmenedeni','meslekideneyimsüresi','bakışaçısı','yurtdışındabulundunuzmu','bakımverdinizmi','bakımvermekistermisiniz','yabancıdilbiliyormusunuz','kültürkonusundaeğitimaldınızmı','yurtdışındaçalışmakistermisiniz','sempozyumkongrekatıldınızmı','zeka1','zeka2','zeka3','zeka4','zeka5','zeka6','zeka7','zeka8','zeka9','zeka10','zeka11','zeka12','zeka13','zeka14','zeka15','zeka16','zeka17','zeka18','zeka19','zeka20','duyarlılık1','duyarlılık2','duyarlılık3','duyarlılık4','duyarlılık5','duyarlılık6','duyarlılık7','duyarlılık8','duyarlılık9','duyarlılık10','duyarlılık11','duyarlılık12','duyarlılık13','duyarlılık14','duyarlılık15','duyarlılık16','duyarlılık17','duyarlılık18','duyarlılık19','duyarlılık20','duyarlılık21','duyarlılık22','duyarlılık23','duyarlılık24']
    data = np.array([liste])
    df2 = pd.DataFrame(data=data,columns=columns)
    df = pd.concat([df,df2],ignore_index = True)
    file = open("C:/Users/m-dur/OneDrive/Masaüstü/kurs.txt","w")
    print(df.to_markdown(),file=file)
    pyreadstat.write_sav(df,'C:/Users/m-dur/OneDrive/Masaüstü/seminer.sav')
    file.close()

