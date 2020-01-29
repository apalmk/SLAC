from itertools import groupby
import numpy as np
from find_duration import find_duration as fd
from collections import Counter
import math
from firebaseconnect import upload
from firebaseconnect import upload1

topics={}
duration= fd("E://projectImplementation//projectFiles//frames//FYP//test_case2.mp4")
# print(duration)
topics[(1,20)]="Particle Swarm Optimization"
topics[(21,60)]="Radial Basis Function"
topics[(61,112)]="Generative Adversarial Networks"


def process_att(a):
    b = range(len(a))
    ll=[]
    for group in groupby(iter(b), lambda x: a[x]):
        if group[0]==0:
            lis=list(group[1])
            ll.append([min(lis), max(lis)])


    # print(ll)
    lenn=len(ll)
    i=0
    fl=[]
    while i<lenn:
        if (ll[i][1]-ll[i][0])>3:
            fl.append([ll[i][0]+1,ll[i][1]+1])
        i=i+1

    return fl

a=np.load('abhishek_attendance_tc2.npy')
abhi_att=process_att(a)
# print(abhi_att)

b=np.load('aman_attendance_tc2.npy')
aman_att=process_att(b)

def find_late_comers(v):
    if v[0][0]==1:
        return "yes"

abh_lc=find_late_comers(abhi_att)
aman_lc=find_late_comers(aman_att)
late_comers=[]
if abh_lc=="yes":
    late_comers.append("Abhishek")

if aman_lc=="yes":
    late_comers.append("Aman")

def find_early_leavers(v):
    ln=len(v)
    if v[ln-1][1]==duration:
        return "yes"

abhi_ear=find_early_leavers(abhi_att)
aman_ear=find_early_leavers(aman_att)
early_leavers=[]
if abhi_ear=="yes":
    early_leavers.append("Abhishek")

if aman_ear=="yes":
    early_leavers.append("Aman")

abhi_emo=np.load('abhishek_emotion_tc2.npy')
aman_emo=np.load('aman_emotion_tc2.npy')



def find_emo_count(value):
    neutral=0
    angry=0
    disgust=0
    happy=0
    surprise=0
    yawn=0
    absent=0
    counter=Counter(value)
    ce=counter.most_common()
    for k in ce:
        if k[0]==-1:
            absent=k[1]
        elif k[0]==0:
            neutral=k[1]
        elif k[0]==1:
            angry=k[1]
        elif k[0]==2:
            disgust=k[1]
        elif k[0]==3:
            happy=k[1]
        elif k[0]==4:
            surprise=k[1]
        elif k[0]==5:
            yawn=k[1]

    return absent,neutral,angry,disgust,happy,surprise,yawn

aman_ab,aman_ne,aman_an,aman_di,aman_ha,aman_su,aman_ya=find_emo_count(aman_emo)
abhi_ab,abhi_ne,abhi_an,abhi_di,abhi_ha,abhi_su,abhi_ya=find_emo_count(abhi_emo)
# print(abhi_ab,abhi_ne,abhi_an,abhi_di,abhi_ha,abhi_su,abhi_ya)

def cls_mood(aman_ab,aman_ne,aman_an,aman_di,aman_ha,aman_su,aman_ya,abhi_ab,abhi_ne,abhi_an,abhi_di,abhi_ha,abhi_su,abhi_ya):
    strr=""
    total=aman_ne+abhi_ne+aman_an+abhi_an+aman_di+abhi_di+aman_ha+abhi_ha+aman_su+abhi_su+aman_ya+abhi_ya
    strr=strr+"neutral: "+str(round((aman_ne+abhi_ne)/total*100,2))+", "
    strr= strr+"angry: "+str(round((aman_an+abhi_an)/total*100,2))+", "
    strr=strr+"disgust: "+str(round((aman_di+abhi_di)/total*100,2))+", "
    strr=strr+"happy: "+str(round((aman_ha+abhi_ha)/total*100,2))+", "
    strr=strr+"surprise: "+str(round((aman_su+abhi_su)/total*100,2))+", "
    strr=strr+"yawning: "+str(round((aman_ya+abhi_ya)/total*100,2))
    return strr

def find_if_attended(n):
    per=n/duration*100
    if per>20:
        return "ab"
    else:
        return "pr"

abhi_pr=find_if_attended(abhi_ab)
aman_pr=find_if_attended(aman_ab)
attendees=[]
if abhi_pr=="pr":
    attendees.append("Abhishek")
if aman_pr=="pr":
    attendees.append("Aman")

def find_missed_topics(att):
    missed=[]
    ln=len(att)
    p=0
    while p<ln:
        c1=att[p][0]
        c2=att[p][1]
        for key, value in topics.items():
            if c1>=key[0] and c1<=key[1]:
                missed.append(topics[key])
            if c2>=key[0] and c2<=key[1]:
                missed.append(topics[key])
        p=p+1
    return set(missed)
abhi_missed=list(find_missed_topics(abhi_att))
# print(abhi_missed)
aman_missed=list(find_missed_topics(aman_att))

def slept_or_no(name,att):
    if name in late_comers:
        if len(att)==1:
            return "not"
        else:
            return "yes"
    if name in early_leavers:
        if len(att)==1:
            return "not"
        else:
            return "yes"

    else:
        return "yes"



# print(aman_missed)
def list_to_str(lst):
    sttr=""
    ln=len(lst)
    u=0
    while u<ln:
        sttr=sttr+str(lst[u])+", "
        u=u+1
    return sttr
LCT=(list(set(abhi_missed) & set(aman_missed)))
class_mood=cls_mood(aman_ab,aman_ne,aman_an,aman_di,aman_ha,aman_su,aman_ya,abhi_ab,abhi_ne,abhi_an,abhi_di,abhi_ha,abhi_su,abhi_ya)
# print(class_mood)
attended=list_to_str(attendees)
abhi_slept=slept_or_no("Abhishek",abhi_att)
aman_slept=slept_or_no("Aman",aman_att)
if abhi_slept=="yes" and aman_slept=="yes":
    slept=2
    wake=0
elif abhi_slept=="not" and aman_slept=="yes":
    slept=1
    wake=1
elif abhi_slept=="not" and aman_slept=="not":
    slept=0
    wake=2
elif abhi_slept=="yes" and aman_slept=="not":
    slept=1
    wake=1

def student_mood(ne,an,di,ha,su,ya):
    stro=""
    all=ne+an+ha+su+ya+di
    stro = stro + "neutral: " + str(round((ne) / all * 100, 2)) + ", "
    stro = stro + "angry: " + str(round((an) / all * 100, 2)) + ", "
    stro = stro + "disgust: " + str(round((di) / all * 100, 2)) + ", "
    stro = stro + "happy: " + str(round((ha) / all * 100, 2)) + ", "
    stro = stro + "surprise: " + str(round((su) / all * 100, 2)) + ", "
    stro = stro + "yawning: " + str(round((ya) / all * 100, 2))
    return stro



sw="slept: "+str(slept)+", wake: "+str(wake)
# print(sw)
lcel="late comers: "+list_to_str(late_comers)+" early leavers: "+list_to_str(early_leavers)
# print(lcel)
# anomaly="Anomaly at "+list_to_str(abn)
abn="None"
LCT=list_to_str(LCT)
# print(LCT)
# print(type(class_mood))
# print(type(abn))
# abn=list_to_str(abn)
# print(type(abn))
if attended=="":
    attended="None"
upload(LCT,class_mood,attended,lcel,abn, sw)
# print((list_to_str(aman_missed)))
# print(aman_pr)
aman_mood=student_mood(aman_ne,aman_an,aman_di,aman_ha,aman_su,aman_ya)
# print(aman_mood)
# print(type(list_to_str(abhi_missed)))
abhi_missed=list_to_str(abhi_missed)
aman_missed=list_to_str(aman_missed)
# print(type(aman_missed))
abhi_mood=student_mood(abhi_ne,abhi_an,abhi_di,abhi_ha,abhi_su,abhi_ya)
# print(abhi_mood)
abhi_sf=np.load('abhishek_sideface_tc2.npy')
aman_sf=np.load('aman_sideface_tc2.npy')
abhi_sf=list_to_str(abhi_sf)
aman_sf=list_to_str(aman_sf)
abhi_mood=abhi_mood+"; Side face at: "+abhi_sf
aman_mood=aman_mood+"; Side Face at: "+aman_sf
upload1("Aman",aman_missed,aman_pr,aman_mood)
# print(anomaly)
upload1("Abhishek",abhi_missed,abhi_pr,abhi_mood)

