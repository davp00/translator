from classes.dictionary import Languaje


class English(Languaje):
    def __init__(self):
        super().__init__()
        self.words = {
            'article': {
                'the'
            },

            'verb': {
                'regular': {
                    'talk',
                    'walk',
                    'add',
                    'earn',
                    'ignored',
                    'join',
                    'call'
                },
                'irregular': {
                    'be',
                    'begin',
                    'bite',
                    'break',
                    'buy',
                    'run',
                    'go',
                    'know',
                    'see'
                }
            },

            'noun': {
                'book',
                'job',
                'car',
                'table',
                'man',
                'number',
                'people'
            },

            'adjective': {
                'happy',
                'tall',
                'good',
                'job',
                'blue'
            },

            'pronoun': {
                'first': {
                    'i'
                },
                'second': {
                    'you',
                },
                'third': {
                    'she',
                    'he',
                    'it'
                },
                'plural': {
                    'they',
                    'we',
                }
            },

            'adverbs': {
                'frequency': {
                    'always',
                    'often',
                    'sometimes',
                    'rarely',
                    'never'
                },
                'place': {
                    'here',
                    'there'
                },
                'way': {
                    'well',
                    'slowly',
                    'quickly'
                }
            }
        }

    def get_grammar(self):
        regular_verbs = self.parse_obj(self.words['verb'].get('regular'))
        irregular_verbs = self.parse_obj(self.words['verb'].get('irregular'))
        verbs = regular_verbs + "| " + irregular_verbs
        articles = self.parse_key('article')
        nouns = self.parse_key('noun')
        adjetives = self.parse_key('adjective')
        # PRONOMBRES
        pro_f = self.parse_obj(self.words['pronoun'].get('first'))
        pro_s = self.parse_obj(self.words['pronoun'].get('second'))
        pro_f_s = pro_f + "| " + pro_s
        pro_third = self.parse_obj(self.words['pronoun'].get('third'))
        pro_plural = self.parse_obj(self.words['pronoun'].get('plural'))

        # ADVERBIOS
        adv_frequency = self.parse_obj(self.words['adverbs'].get('frequency'))

        self.grammar = """
        
            sentence: present_simple_af         -> presente_simple_afirmativo
            | present_simple_ne                 -> presente_simple_negativo
            | present_simple_interrogative      -> presente_simple_interrogativo
            | tp_present_simple_af              -> presente_simple_tercera_persona_afirmativo
            | tp_present_simple_ne              -> presente_simple_tercera_persona_negativo
            | tp_present_simple_interrogative   -> presente_simple_tercera_persona_interrogativo
            | article                           -> articulo
            | verb                              -> verbo
            | tp_verb                           -> verbo_tercera_persona
            | noun                              -> sustantivo
            | pro_f_s                           -> pronombre_primera_o_segunda_persona
            | pro_third                         -> pronombre_tercera_persona
            | adj                               -> adjetivo
            
            // PRESENTE SIMPLE
                present_simple_af:  pro_f_s (adv_freq)? verb
                                    | article noun to_be_t adj
                                    | pro_f to_be_f adj
                                    | pro_s to_be_s adj
                                    | pro_plural to_be_plural adj
                                    
                present_simple_ne: pro_f_s ne_fs_auxverb verb
                
                present_simple_interrogative: af_fs_auxverb pro_f_s verb sym_interrogative
            ///
            
            // PRESENTE SIMPLE Tercera persona
                tp_present_simple_af: pro_third (adv_freq)? tp_verb
                                    | pro_third to_be_t adj 
                                        
                tp_present_simple_ne: pro_third ne_tp_auxverb verb
                
                tp_present_simple_interrogative: af_tp_auxverb pro_third verb sym_interrogative
            ///
            
            // BASICS
                article: ARTICLE
                verb: VERB
                noun: NOUN
                popper_noun: POPPER_NOUN
                adj: ADJ
                object: NOUN | POPPER_NOUN
                sym_interrogative: SYMBOL_INTERROGATIVE
                pro_f: PRONOUN_F
                pro_s: PRONOUN_S
                pro_third: PRONOUN_THIRD
                pro_plural: PRONOUN_PLURAL
                to_be_f: TO_BE_F
                to_be_s: TO_BE_S
                to_be_t: TO_BE_T
                to_be_plural: TO_BE_PLU
                adv_freq: ADV_FREQUENCY
            ///
            
            /// DERIVADOS PRIMERA/SEGUNDA PERSONA
                pro_f_s: PRONOUN_F_S
                
                af_fs_auxverb: AF_FS_AUXVERB
                ne_fs_auxverb: NE_FS_AUXVERB
            //
            
            /// DERIVADOS TERCERA PERSONA
                tp_verb: VERB + "s"
                af_tp_auxverb: AF_TP_AUXVERB
                ne_tp_auxverb: NE_TP_AUXVERB
            //
            
            OBJECT: NOUN
            ARTICLE: {}
            VERB: {}
            NOUN: {}
            ADJ: {}
            POPPER_NOUN: WORD
            PRONOUN_F_S: {}
            PRONOUN_F: {}
            PRONOUN_S: {}
            PRONOUN_THIRD: {}
            PRONOUN_PLURAL: {}
            
            ADV_FREQUENCY: {}
            
            TO_BE_F: "am"
            TO_BE_S: "are"
            TO_BE_T: "is"
            
            TO_BE_PLU: TO_BE_S
            
            // AUXILIARES 
                AF_FS_AUXVERB: "do"
                NE_FS_AUXVERB: "dont"
                
                AF_TP_AUXVERB: "does"
                NE_TP_AUXVERB: "doesnt"
            ///
            SYMBOL_INTERROGATIVE: "?"
            
            %import common.WS
            %import common.WORD  
            %ignore " "
            %ignore WS
        """.format(
            # BASICS
            articles,
            verbs,
            nouns,
            adjetives,
            # PRONOMBRES
            pro_f_s,
            pro_f,
            pro_s,
            pro_third,
            pro_plural,
            # ADVERBIOS
            adv_frequency
            )

        return self.grammar