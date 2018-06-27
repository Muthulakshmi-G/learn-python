from sklearn.feature_extraction import DictVectorizer
import statistics as stats

x=[1,2,3,4,5,6,7,8,9]
y=[2,1,2,4.5,7,6.5,6,9,9.5]

def pearson(x,y):

    n=len(x)

    score_x=[]
    score_y=[]


    mean_x=stats.mean(x)
    mean_y=stats.mean(y)

    sd_x=stats.stdev(x)

    sd_y=stats.stdev(y)

    for observation in x:
        score_x.append((observation-mean_x)/sd_x)

    for obseervation in y:
         score_y.append((observation-mean_y)/sd_y)

    return (sum([i*j for i,j in zip(score_x,score_y)]))/(n-1)
        
print(pearson(x,y))



#################

staff=[{'name': 'Steve Miller', 'age': 33.},
         {'name': 'Lyndon Jones', 'age': 12.},
         {'name': 'Baxter Morth', 'age': 18.}]


vec=DictVectorizer()
vec.fit_transform(staff).toarray()

print(vec.get_feature_names())

