import flet as ft
import networkx as nx


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        try:
            anno_input = int(self._view._txtAnno.value)
        except ValueError:
            self._view.create_alert('Inserire un intero')
            return

        if not 1816 < anno_input < 2006:
            self._view.create_alert("L'anno dev'essere tra il 1816 e il 2006")
            return

        self._model.creaGrafo(anno_input)
        self._view._txt_result.controls.append(ft.Text(f'Grafo correttamente creato {self._model.grafo}'))
        self._view._txt_result.controls.append(ft.Text(f'Il grafo ha {nx.number_connected_components(self._model.grafo)} componenti connesse'))
        for node, degree in self._model.grafo.degree:
            self._view._txt_result.controls.append(
                ft.Text(f'{node} -- {degree} vicini'))

        self._view.popola_ddState()
        self._view._ddState.value = None
        self._view.update_page()

    def handleRaggiungibili(self, e):
        self._view._txt_result.controls.clear()
        stato = self._view._ddState.value
        if stato is None:
            self._view.create_alert('selezionare uno stato')
            return
        self._model.calcolaPercorso(stato)
        print(self._model.raggiungibili)
