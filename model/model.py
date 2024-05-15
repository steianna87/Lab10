import copy

import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self.countryList = DAO.getAllCountry()
        self.idMap = {}
        for c in self.countryList:
            self.idMap[c.CCode] = c

        self.grafo = nx.Graph()
        self.connessioni = None

        self.raggiungibili = None
        self.raggiungibili_ricorsivo = set()
        self.raggiungibili_iterativo = None

    def creaGrafo(self, year):
        self.grafo.clear()
        # self.grafo.add_nodes_from(DAO.getAllCountry_by_year(year))

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
        self.raggiungibili = nx.node_connected_component(self.grafo, stato)

    def calcolaPercorsoRicorsivo(self, stato):
        self.raggiungibili_ricorsivo.clear()
        self.ricorsione(stato, None)

    def calcolaPercorsoIterativo(self, stato):
        visitati = set()
        da_visitare = [stato]
        while len(da_visitare) > 0:
            visitato = da_visitare[0]
            visitati.add(visitato)
            vicini = [vicino for vicino in self.grafo[visitato] if vicino not in visitati]
            da_visitare.extend(vicini)
            da_visitare.pop(0)
        self.raggiungibili_iterativo = visitati

    def ricorsione(self, stato, precedente):
        if len(self.grafo[stato]) == 1 and precedente in self.grafo[stato]:
            return
        else:
            for vicino in self.grafo[stato]:
                if vicino not in self.raggiungibili_ricorsivo:
                    self.raggiungibili_ricorsivo.add(vicino)
                    self.ricorsione(vicino, stato)
