import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self.countryList = DAO.getAllCountry()
        self.idMap = {}
        for c in self.countryList:
            self.idMap[c.CCode] = c

        self.grafo = nx.Graph()
        self.connessioni = []

        self.raggiungibili = None

    def creaGrafo(self, year):
        self.grafo.clear()
        #self.grafo.add_nodes_from(DAO.getAllCountry_by_year(year))

        contiguity = DAO.getContiguity(year)
        for confine in contiguity:
            country1 = self.idMap[confine.state1no]
            country2 = self.idMap[confine.state2no]
            self.grafo.add_node(country1)
            self.grafo.add_node(country2)
            if confine.conttype == 1:
                self.grafo.add_edge(country1, country2)

        self.connessioni = nx.connected_components(self.grafo)

    def calcolaPercorso(self, stato):
        '''self.raggiungibili = nx.node_connected_component(self.grafo, stato)'''
        pass



