from telecomapp import node as n
import telecomapp.net as net

if __name__ == '__main__':
    my_node = n.Node("aga001")
    arr = net.csv_to_arr('H:/workspace/python/telecom-project/data/BD Routage 30 10 2021.csv')
    my_net = net.Net(arr)
    my_net.gen_json(my_net.get_nodes()['FO'])
    # for i in np.arange(0, len(my_net.get_nodes()['FO'].get_child())):
    # print(my_net.get_nodes()['FO'].get_child()[i].get_label())
    # my_net.gen_json(my_net.get_nodes()['FO'])
    # print(my_net.str_tree)
    file = open("copy.txt", "w")
    file.write(my_net.str_tree)
    file.close()
