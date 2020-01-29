
def upload(lct,md,att,lcel,abn,sw):
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://slac-d7d0b.firebaseio.com/', None)
    data =  { 'lct1': lct,
              'mood': md,
              'att': att,
              'lcel': lcel,
              'abn': abn,
              'sa': sw
            # date,time,students present
            }
    result = firebase.post('/Classes/',data)
    print(result)

def upload1(name,miss,atten,mood1):
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://slac-d7d0b.firebaseio.com/', None)
    data =  { 'name': name,
              'mood': mood1,
              'atten': atten,
              'miss': miss
            # date,time,students present
            }
    result = firebase.post('/class/',data)
    print(result)