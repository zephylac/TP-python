def ajoute(mot1,mot2,d) :
        if(!(d.has-key(mot1))) :
                d.update(mot1: mot2)
                print "Le mot à été ajouté dans le dictionnaire"
        else :
                print "Le mot est déjà présent dans le dictionnaire"

def affiche(d) :
        a = []
        a = d.keys
        for i in len(a)
                print "Mot FR : " + a[i] + " -> Mot EN : " + d[a[i]]
        
def delete(char,d) :
        a = []
        a = d.keys
        for i in len(a)
                if a[i][0:1] == char
                        del(d[a[i]])




d = {"bonjour" : "hello","au revoir" : "goodbye","travail" : "work","fainéant" : "lazy", "école" : "school"}
print d
d.update({"rire" : "laugh"})
print d

print "dictionnary has key 'rire' :" + d.has-key("rire")


