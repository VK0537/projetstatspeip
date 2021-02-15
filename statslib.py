from fractions import Fraction
import numpy as np
# from decimal import Decimal, ROUND_HALF_UP

class Stat():
    def __init__(self,stat,pStart=0,pEnd=None,pStep=1):
        if(isinstance(stat,list)):
            if(pStart==None):pStart=0
            if(pEnd==None):pEnd=len(stat)
            self.serie=stat
        # self.pop=np.arange(pStart,pEnd,pStep).tolist()
        elif(callable(stat)):
            try:self.serie=[stat(i) for i in np.arange(pStart,pEnd,pStep)]
            except:raise
        self.N=len(np.arange(pStart,pEnd,pStep))
        self.moda=sorted(list(dict.fromkeys(self.serie))) # <- modalites
    def __repr__(self):return(
        f"Valeur   |{'|'.join([str(Fraction(i).limit_denominator()) for i in self.moda])}\n"+
        f"Effectif |{'|'.join([' '*(len(str(Fraction(self.moda[i-1]).limit_denominator()))-1)+str(self.ef(i)) for i in range(1,len(self.moda)+1)])}\n\n"+
        f"Moyenne : {self.moy()}\nEcart-type : {self.ecarttyp()}\n")
        # repr renvoie lors du print un tableau avec les modalites dans l'ordre croissant
        # et leur effectif.
    def ef(self,n):     return sum(1 for i in self.serie if i==self.moda[n-1] and n>0)
        # ef renvoie l'effectif d'une certaine valeur
    def efC(self,n):    return sum(self.ef(i) for i in range(1,n+1))
        # efC fait la somme des effectifs pour les valeurs inferieures ou egales
    def fr(self,n):     return (self.ef(n)/self.N if n>0 else 0)
        # fr renvoie la frequence a laquelle aparait une valeur donnee
    def frC(self,n):    return sum(self.fr(i) for i in range(1,n+1))
        # frC fait le somme des frequences pour les valeurs inferieures ou egales
    def mode(self):     return [self.moda[i-1] for i in range(len(self.moda)) if self.ef(i)==max([self.ef(j) for j in range(1,len(self.moda)+1)])]
        # mode renvoie la valeur la plus fréquente
    def med(self):      return self.quan(2)[0]
            # l=len(self.serie())
            # s=sorted(self.serie())
            # return (s[l//2] if l%2!=0 else (s[l//2]+s[l//2-1])/2)
        # med renvoie la médiane : la valeur de la serie telle qu'il y a autant de valeurs 
        # d'un cote que de l'autre (suivie d'une autre facon, sans utiliser les quantiles)
    def quan(self,n):
        q=[]
        s=sorted(self.serie)
        for i in range(1,n):
            a=(i*len(s)/n)
            b=(a-a%.5+.5 if (a%.5<.25 if a>len(s)/2 else a%.5<=.25) else a-a%.5+1)
            q.append(s[int(b)-1] if b%1==0 else (s[int(b)]+s[int(b)-1])/2)
        return q
            # def quan(self,n):return [(sorted(self.serie)[int(((i*len(sorted(self.serie))/n)-(i*len(sorted(self.serie))/n)%.5+.5 if ((i*len(sorted(self.serie))/n)%.5<.25 if (i*len(sorted(self.serie))/n)>len(sorted(self.serie))/2 else (i*len(sorted(self.serie))/n)%.5<=.25) else (i*len(sorted(self.serie))/n)-(i*len(sorted(self.serie))/n)%.5+1))-1] if ((i*len(sorted(self.serie))/n)-(i*len(sorted(self.serie))/n)%.5+.5 if ((i*len(sorted(self.serie))/n)%.5<.25 if (i*len(sorted(self.serie))/n)>len(sorted(self.serie))/2 else (i*len(sorted(self.serie))/n)%.5<=.25) else (i*len(sorted(self.serie))/n)-(i*len(sorted(self.serie))/n)%.5+1)%1==0 else (sorted(self.serie)[int(((i*len(sorted(self.serie))/n)-(i*len(sorted(self.serie))/n)%.5+.5 if ((i*len(sorted(self.serie))/n)%.5<.25 if (i*len(sorted(self.serie))/n)>len(sorted(self.serie))/2 else (i*len(sorted(self.serie))/n)%.5<=.25) else (i*len(sorted(self.serie))/n)-(i*len(sorted(self.serie))/n)%.5+1))]+sorted(self.serie)[int(((i*len(sorted(self.serie))/n)-(i*len(sorted(self.serie))/n)%.5+.5 if ((i*len(sorted(self.serie))/n)%.5<.25 if (i*len(sorted(self.serie))/n)>len(sorted(self.serie))/2 else (i*len(sorted(self.serie))/n)%.5<=.25) else (i*len(sorted(self.serie))/n)-(i*len(sorted(self.serie))/n)%.5+1))-1])/2) for i in range(1,n)]
        # quan renvoie les quantiles d'ordre n : les valeurs séparant la série en n parties
        # de meme effectif
    def moy(self):      return self.mmt(1)#sum(i for i in self.serie)/self.N
        # moy rnevoie la moyenne arithmetique de la serie : la somme des valeurs divisee 
        # par la taille de l'echantillon
    def etendue(self):  return max(i for i in self.serie)-min(i for i in self.serie)
        # etendue renvoie l'ecart entre la plus petite et la plus grande valeur de la serie
    def ecartmoy(self): return sum(abs(i-self.mmt(1)) for i in self.serie)/self.N
        # ecartmoy renvoie l'ecart moyen : la dispersion des valeurs autour de la moyenne
    def variance(self): return self.mmtctr(2)#sum((i-self.mmt(1))**2 for i in self.serie)/self.N
        # variance donne la variance de la serie, utilisee pour calculer l'ecart type
    def ecarttyp(self): return (abs(self.variance()))**(1/2)
        # ecarttyp donne l'ecart type, une mesure de disperssion des valeurs
    # NB : apres des recherches, pour obtenir le meme resultat que les methodes de scipy et 
        # statistics, il faudrait appliquer un facteur de correction de n/(n-1) pour eviter
        # des erreurs s'accumulant a chaque iterations : 
    def variance2(self): return sum(((i-self.mmt(1))**2)*(self.N/(self.N-1)) for i in self.serie)/self.N
    def ecarttyp2(self): return (abs(self.variance2()))**(1/2)
        # corrigés a n/(n-1)
    def mmt(self,k):    return sum(i**k for i in self.serie)/self.N
        # mmt donne le moment d'ordre k, une autre valeur de disperssion
    def mmtctr(self,k): return sum((i-self.mmt(1))**k for i in self.serie)/self.N
        # mmtctr donne le moment centre d'ordre k, cette fois ci autour de la moyenne
    # def mmt(self,k):    return sum(i**k for i in self.serie)/self.N
    # def mmtctr(self,k): return sum((i-self.mmt(1))**k for i in self.serie)/self.N

    def asym(self):     return (self.mmtctr(3)/self.ecarttyp()**3)
    def apla(self):     return (self.mmtctr(4)/self.ecarttyp()**4)
