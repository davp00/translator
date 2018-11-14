from classes.dictionary import Languaje


class English(Languaje):
    def __init__(self):
        super().__init__()
        self.words = {
            'article': {
                'the'
            },

            'verb': {
                'run',
                'eat',
                'play',
                'walk',
                'see',
                'teach',
                'talk'
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
                'job'
            },

            'pronoun': {
                'first/second': {
                    'i',
                    'you',
                },
                'third': {
                    'she',
                    'he',
                    'it'
                }
            }
        }

    def get_grammar(self):

        verbs = self.parse_key('verb')
        articles = self.parse_key('article')
        nouns = self.parse_key('noun')
        adjetives = self.parse_key('adjective')
        pro_f_s = self.parse_obj(self.words['pronoun'].get('first/second'))
        pro_third = self.parse_obj(self.words['pronoun'].get('third'))

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
            
            // Primera o segunda persona
                present_simple_af: pro_f_s verb
                present_simple_ne: pro_f_s ne_fs_auxverb verb
                
                present_simple_interrogative: af_fs_auxverb pro_f_s verb sym_interrogative
            ///
            
            // Tercera persona
                tp_present_simple_af: pro_third tp_verb
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
            ///
            
            /// DERIVADOS PRIMERA/SEGUNDA PERSONA
                pro_f_s: PRONOUN_F_S
                pro_third: PRONOUN_THIRD
                
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
            PRONOUN_THIRD: {}
            
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
            articles,
            verbs,
            nouns,
            adjetives,
            pro_f_s,
            pro_third)

        return self.grammar