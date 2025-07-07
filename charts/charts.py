#Modulo


import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A','B', 'C']
    values = [50, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.show()
    #plt.savefig('pie.png') #para genera imagen 
    plt.close()

