'''
Defines a class, Neuron472352327, of neurons from Allen Brain Institute's model 472352327

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472352327:
    def __init__(self, name="Neuron472352327", x=0, y=0, z=0):
        '''Instantiate Neuron472352327.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472352327_instance is used instead
        '''
        
        # load the morphology
        from load_swc import load_swc
        load_swc('Htr3a-Cre_NO152_Ai14_IVSCC_-175482.03.02.01_475124358_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
        
        self._name = name
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472352327_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im_v2', u'K_T', u'Kd', u'Kv2like', u'Kv3_1', u'NaV', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 67.11
            sec.e_pas = -87.4209747314
        
        for sec in self.axon:
            sec.cm = 2.3
            sec.g_pas = 0.000877965239702
        for sec in self.dend:
            sec.cm = 2.3
            sec.g_pas = 2.38788417905e-05
        for sec in self.soma:
            sec.cm = 2.3
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Ih = 0.000122653
            sec.gbar_NaV = 0.0664205
            sec.gbar_Kd = 5.30709e-05
            sec.gbar_Kv2like = 2.04034e-05
            sec.gbar_Kv3_1 = 0.168562
            sec.gbar_K_T = 0.000140197
            sec.gbar_Im_v2 = 0.00506731
            sec.gbar_SK = 0.00011628
            sec.gbar_Ca_HVA = 0.000337475
            sec.gbar_Ca_LVA = 0.00891093
            sec.gamma_CaDynamics = 0.037713
            sec.decay_CaDynamics = 795.904
            sec.g_pas = 5.72175e-05
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

