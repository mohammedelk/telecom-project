from telecomapp import node as n
from telecomapp import net

if __name__ == '__main__':
    my_node = n.Node("aga001")
    arr = net.csv_to_arr('../data/BD Routage 30 10 2021.csv')
    my_net = net.Net(arr)
    print(my_net.get_nodes())
