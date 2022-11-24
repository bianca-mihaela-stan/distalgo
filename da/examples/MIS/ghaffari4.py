# -*- generated by 1.2.0b2 -*-
import da
PatternExpr_330 = da.pat.TuplePattern([da.pat.ConstantPattern('hi'), da.pat.FreePattern('index'), da.pat.FreePattern('id')])
PatternExpr_348 = da.pat.TuplePattern([da.pat.ConstantPattern('done'), da.pat.FreePattern('index'), da.pat.FreePattern('node_mis')])
PatternExpr_568 = da.pat.TuplePattern([da.pat.ConstantPattern('start round'), da.pat.FreePattern('round_nr')])
PatternExpr_878 = da.pat.ConstantPattern('confirmation1')
PatternExpr_882 = da.pat.BoundPattern('_BoundPattern883_')
PatternExpr_1100 = da.pat.TuplePattern([da.pat.ConstantPattern('desire_level + mark'), da.pat.FreePattern('desire_level'), da.pat.FreePattern('mis'), da.pat.FreePattern('index'), da.pat.FreePattern('round_nr')])
PatternExpr_1113 = da.pat.FreePattern('source')
PatternExpr_1157 = da.pat.TuplePattern([da.pat.ConstantPattern('i am in the mis'), da.pat.FreePattern('index'), da.pat.FreePattern('mis'), da.pat.FreePattern('round_nr')])
PatternExpr_1168 = da.pat.FreePattern('source')
PatternExpr_1207 = da.pat.TuplePattern([da.pat.ConstantPattern('i am not in the mis'), da.pat.FreePattern('index'), da.pat.FreePattern('mis'), da.pat.FreePattern('round_nr')])
PatternExpr_1218 = da.pat.FreePattern('source')
PatternExpr_1259 = da.pat.TuplePattern([da.pat.ConstantPattern('confirmation1'), da.pat.FreePattern('round_nr')])
PatternExpr_1266 = da.pat.FreePattern('source')
PatternExpr_1299 = da.pat.TuplePattern([da.pat.ConstantPattern('confirmation2'), da.pat.FreePattern('round_nr')])
PatternExpr_1306 = da.pat.FreePattern('source')
PatternExpr_1339 = da.pat.TuplePattern([da.pat.ConstantPattern('confirmation3'), da.pat.FreePattern('round_nr')])
PatternExpr_1346 = da.pat.FreePattern('source')
PatternExpr_884 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern890_')]), da.pat.ConstantPattern('confirmation1')])
_config_object = {'handling': 'one', 'channel': 'reliable'}
import da
import sys
import random
import os
import copy
f = open('/home/bianca/distAlgo/distalgo/da/examples/MIS/graph4.txt')
f2 = open('/home/bianca/distAlgo/distalgo/da/examples/MIS/found_mis.txt', 'w')

class Coordinator(da.DistProcess):

    def __init__(self, procimpl, forwarder, **props):
        super().__init__(procimpl, forwarder, **props)
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_CoordinatorReceivedEvent_0', PatternExpr_330, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Coordinator_handler_329]), da.pat.EventPattern(da.pat.ReceivedEvent, '_CoordinatorReceivedEvent_1', PatternExpr_348, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Coordinator_handler_347])])

    def setup(self, nr_nodes, **rest_1532):
        super().setup(nr_nodes=nr_nodes, **rest_1532)
        self._state.nr_nodes = nr_nodes
        self._state.nodes = {}
        self._state.nr_nodes = self._state.nr_nodes
        self._state.mis = []
        self._state.ack = 0
        self._state.keep_going = True
        self._state.round_nr = 0
        self._state.await_ack_from_nr = 0

    def run(self):
        super()._label('_st_label_236', block=False)
        _st_label_236 = 0
        while (_st_label_236 == 0):
            _st_label_236 += 1
            if (len(self._state.nodes.keys()) == (self._state.nr_nodes - 1)):
                _st_label_236 += 1
            else:
                super()._label('_st_label_236', block=True)
                _st_label_236 -= 1
        self._state.initial_nodes = copy.deepcopy(self._state.nodes)
        while (self._state.keep_going == True):
            self._state.await_ack_from_nr = len(list(self._state.nodes.keys()))
            self._state.keep_going = False
            self._state.ack = 0
            self._state.round_nr += 1
            self.send(('start round', self._state.round_nr), to=list(self._state.nodes.values()))
            self.output('awaiting ack')
            super()._label('_st_label_311', block=False)
            _st_label_311 = 0
            while (_st_label_311 == 0):
                _st_label_311 += 1
                if (self._state.ack == self._state.await_ack_from_nr):
                    _st_label_311 += 1
                else:
                    super()._label('_st_label_311', block=True)
                    _st_label_311 -= 1
            else:
                if (_st_label_311 != 2):
                    continue
            if (_st_label_311 != 2):
                break
            self.output('after awaiting ack')
        self.output(self._state.mis)

    def _Coordinator_handler_329(self, index, id):
        self._state.nodes[index] = id
    _Coordinator_handler_329._labels = None
    _Coordinator_handler_329._notlabels = None

    def _Coordinator_handler_347(self, index, node_mis):
        self.output(f'coordinator {self._state.round_nr}: received {node_mis} from {index}')
        if (index in list(self._state.nodes.keys())):
            self._state.ack += 1
        if (node_mis == 'IN MIS'):
            self._state.mis.append(index)
        if ((node_mis == 'IN MIS') or (node_mis == 'NOT IN MIS')):
            self._state.nodes.pop(index)
        if (node_mis == 'NOT DECIDED'):
            self._state.keep_going = True
    _Coordinator_handler_347._labels = None
    _Coordinator_handler_347._notlabels = None

class P(da.DistProcess):

    def __init__(self, procimpl, forwarder, **props):
        super().__init__(procimpl, forwarder, **props)
        self._PReceivedEvent_1 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_0', PatternExpr_568, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_567]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_1', PatternExpr_878, sources=[PatternExpr_882], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_2', PatternExpr_1100, sources=[PatternExpr_1113], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_1099]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_3', PatternExpr_1157, sources=[PatternExpr_1168], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_1156]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_4', PatternExpr_1207, sources=[PatternExpr_1218], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_1206]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_5', PatternExpr_1259, sources=[PatternExpr_1266], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_1258]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_6', PatternExpr_1299, sources=[PatternExpr_1306], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_1298]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_7', PatternExpr_1339, sources=[PatternExpr_1346], destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_1338])])

    def setup(self, index, neighbors_indexes, neighbors_process_ids, coordinator, **rest_1532):
        super().setup(index=index, neighbors_indexes=neighbors_indexes, neighbors_process_ids=neighbors_process_ids, coordinator=coordinator, **rest_1532)
        self._state.index = index
        self._state.neighbors_indexes = neighbors_indexes
        self._state.neighbors_process_ids = neighbors_process_ids
        self._state.coordinator = coordinator
        self._state.index = self._state.index
        self._state.neighbors = {self._state.neighbors_indexes[i]: self._state.neighbors_process_ids[i] for i in range(len(self._state.neighbors_indexes))}
        self._state.coordinator = self._state.coordinator
        self._state.MIS = 'NOT DECIDED'
        self._state.desire_level = 0.5
        self._state.effective_degree = None
        self._state.desire_marks = {}
        self._state.round_nr = 1
        self._state.confirmation1 = {}
        self._state.confirmation2 = {}
        self._state.confirmation3 = {}
        self._state.received_mis = {}
        self._state.expect_confirmation_from = 0
        self._state.mis_from_neighbors = {}
        self._state.not_mis_from_neighbors = {}

    def run(self):
        self.send(('hi', self._state.index, self._id), to=self._state.coordinator)
        self.output(f'{self._state.index} : {self._state.neighbors}')
        super()._label('_st_label_563', block=False)
        _st_label_563 = 0
        while (_st_label_563 == 0):
            _st_label_563 += 1
            if ():
                _st_label_563 += 1
            else:
                super()._label('_st_label_563', block=True)
                _st_label_563 -= 1

    def _P_handler_567(self, round_nr):
        self._state.round_nr = round_nr
        self._state.expect_confirmation_from = len(list(self._state.neighbors.items()))
        self.output(f'{self._state.index} : starting round {self._state.round_nr}')
        if (not (self._state.round_nr in list(self._state.mis_from_neighbors.keys()))):
            self._state.mis_from_neighbors[self._state.round_nr] = {}
        if (not (self._state.round_nr in list(self._state.not_mis_from_neighbors.keys()))):
            self._state.not_mis_from_neighbors[self._state.round_nr] = {}
        if (not (self._state.round_nr in list(self._state.desire_marks.keys()))):
            self._state.desire_marks[self._state.round_nr] = []
        if (not (self._state.round_nr in list(self._state.confirmation1.keys()))):
            self._state.confirmation1[self._state.round_nr] = []
        if (not (self._state.round_nr in list(self._state.confirmation2.keys()))):
            self._state.confirmation2[self._state.round_nr] = []
        if (not (self._state.round_nr in list(self._state.confirmation3.keys()))):
            self._state.confirmation3[self._state.round_nr] = []
        if (not (self._state.round_nr in list(self._state.received_mis.keys()))):
            self._state.received_mis[self._state.round_nr] = []
        if ((self._state.round_nr - 1) in list(self._state.desire_marks.keys())):
            self._state.effective_degree = sum([x[0] for x in self._state.desire_marks[(self._state.round_nr - 1)]])
            if (self._state.effective_degree >= 2):
                self._state.desire_level = (self._state.desire_level / 2)
            else:
                self._state.desire_level = min((2 * self._state.desire_level), 0.5)
        self._state.MIS = random.choices(['IN MIS', 'NOT DECIDED'], weights=[self._state.desire_level, (1 - self._state.desire_level)])[0]
        self.send(('desire_level + mark', self._state.desire_level, self._state.MIS, self._state.index, self._state.round_nr), to=list(self._state.neighbors.values()))
        super()._label('_st_label_863', block=False)
        p = None

        def UniversalOpExpr_864():
            nonlocal p
            for p in list(self._state.neighbors.values()):
                if (not PatternExpr_884.match_iter(self._PReceivedEvent_1, _BoundPattern890_=p, SELF_ID=self._id)):
                    return False
            return True
        _st_label_863 = 0
        while (_st_label_863 == 0):
            _st_label_863 += 1
            if UniversalOpExpr_864():
                _st_label_863 += 1
            else:
                super()._label('_st_label_863', block=True)
                _st_label_863 -= 1
        super()._label('_st_label_894', block=False)
        _st_label_894 = 0
        while (_st_label_894 == 0):
            _st_label_894 += 1
            if (len(self._state.desire_marks[self._state.round_nr]) == self._state.expect_confirmation_from):
                _st_label_894 += 1
            else:
                super()._label('_st_label_894', block=True)
                _st_label_894 -= 1
        if (('IN MIS' in [x[1] for x in self._state.desire_marks[self._state.round_nr]]) and (self._state.MIS == 'IN MIS')):
            self.output('got here')
            self._state.MIS = 'NOT DECIDED'
        self.send(('i am in the mis', self._state.index, self._state.MIS, round_nr), to=list(self._state.neighbors.values()))
        super()._label('_st_label_957', block=False)
        _st_label_957 = 0
        while (_st_label_957 == 0):
            _st_label_957 += 1
            if (len(self._state.confirmation2[self._state.round_nr]) == self._state.expect_confirmation_from):
                _st_label_957 += 1
            else:
                super()._label('_st_label_957', block=True)
                _st_label_957 -= 1
        super()._label('_st_label_971', block=False)
        _st_label_971 = 0
        while (_st_label_971 == 0):
            _st_label_971 += 1
            if (len(list(self._state.mis_from_neighbors[self._state.round_nr].keys())) == self._state.expect_confirmation_from):
                _st_label_971 += 1
            else:
                super()._label('_st_label_971', block=True)
                _st_label_971 -= 1
        if ('IN MIS' in self._state.mis_from_neighbors[self._state.round_nr].values()):
            self._state.MIS = 'NOT IN MIS'
        self.send(('i am not in the mis', self._state.index, self._state.MIS, round_nr), to=list(self._state.neighbors.values()))
        super()._label('_st_label_1024', block=False)
        _st_label_1024 = 0
        while (_st_label_1024 == 0):
            _st_label_1024 += 1
            if (len(self._state.confirmation3[self._state.round_nr]) == self._state.expect_confirmation_from):
                _st_label_1024 += 1
            else:
                super()._label('_st_label_1024', block=True)
                _st_label_1024 -= 1
        super()._label('_st_label_1038', block=False)
        _st_label_1038 = 0
        while (_st_label_1038 == 0):
            _st_label_1038 += 1
            if (len(list(self._state.not_mis_from_neighbors[self._state.round_nr].keys())) == self._state.expect_confirmation_from):
                _st_label_1038 += 1
            else:
                super()._label('_st_label_1038', block=True)
                _st_label_1038 -= 1
        for (key, value) in list(self._state.not_mis_from_neighbors[self._state.round_nr].items()):
            if (value == 'NOT IN MIS'):
                self._state.neighbors.pop(key)
        self.send(('done', self._state.index, self._state.MIS), to=self._state.coordinator)
    _P_handler_567._labels = None
    _P_handler_567._notlabels = None

    def _P_handler_1099(self, desire_level, mis, index, round_nr, source):
        if (round_nr in list(self._state.desire_marks.keys())):
            self._state.desire_marks[round_nr].append([desire_level, mis, index])
        else:
            self._state.desire_marks[round_nr] = [[desire_level, mis, index]]
        self.send(('confirmation1', round_nr), to=source)
    _P_handler_1099._labels = None
    _P_handler_1099._notlabels = None

    def _P_handler_1156(self, index, mis, round_nr, source):
        if (round_nr in list(self._state.mis_from_neighbors.keys())):
            self._state.mis_from_neighbors[round_nr][index] = mis
        else:
            self._state.mis_from_neighbors[round_nr] = {index: mis}
        self.send(('confirmation2', round_nr), to=source)
    _P_handler_1156._labels = None
    _P_handler_1156._notlabels = None

    def _P_handler_1206(self, index, mis, round_nr, source):
        if (self._state.round_nr in list(self._state.not_mis_from_neighbors.keys())):
            self._state.not_mis_from_neighbors[round_nr][index] = mis
        else:
            self._state.not_mis_from_neighbors[round_nr] = {index: mis}
        self.send(('confirmation3', round_nr), to=source)
    _P_handler_1206._labels = None
    _P_handler_1206._notlabels = None

    def _P_handler_1258(self, round_nr, source):
        if (not (round_nr in list(self._state.confirmation1.keys()))):
            self._state.confirmation1[round_nr] = [source]
        else:
            self._state.confirmation1[round_nr].append(source)
    _P_handler_1258._labels = None
    _P_handler_1258._notlabels = None

    def _P_handler_1298(self, round_nr, source):
        if (not (round_nr in list(self._state.confirmation2.keys()))):
            self._state.confirmation2[round_nr] = [source]
        else:
            self._state.confirmation2[round_nr].append(source)
    _P_handler_1298._labels = None
    _P_handler_1298._notlabels = None

    def _P_handler_1338(self, round_nr, source):
        if (not (round_nr in list(self._state.confirmation3.keys()))):
            self._state.confirmation3[round_nr] = [source]
        else:
            self._state.confirmation3[round_nr].append(source)
    _P_handler_1338._labels = None
    _P_handler_1338._notlabels = None

class Node_(da.NodeProcess):

    def __init__(self, procimpl, forwarder, **props):
        super().__init__(procimpl, forwarder, **props)
        self._events.extend([])

    def run(self):
        dict = {}
        line = f.readline()
        n = 1
        while line:
            line = line.strip('\n')
            list = line.split(' ')
            x = list[0]
            self.output(list)
            dict[n] = [int(x) for x in list[2:(- 1)]]
            line = f.readline()
            n += 1
        ps = []
        for i in range(1, n):
            p = self.new(P, method='thread')
            ps.append(p)
        self.output(dict)
        coordinator = self.new(Coordinator)
        self._setup({coordinator}, (n,))
        self._start(coordinator)
        for (i, p) in enumerate(ps):
            ps_ids = []
            for x in dict[(i + 1)]:
                ps_ids.append(ps[(x - 1)])
            self._setup({p}, ((i + 1), tuple(dict[(i + 1)]), tuple(ps_ids), coordinator))
        self._start(ps)
