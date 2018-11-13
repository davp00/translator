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
            sentence: pro_third 
            | present_simple_afirmative
            
            present_simple_afirmative: noun verb
            
            article: ARTICLE
            verb: VERB
            noun: NOUN
            popper_noun: POPPER_NOUN
            pro_f_s: PRONOUN_F_S
            pro_third: PRONOUN_THIRD
            adj: ADJ
        
            ARTICLE: {}
            VERB: {}
            NOUN: {}
            ADJ: {}
            POPPER_NOUN: WORD
            PRONOUN_F_S: {}
            PRONOUN_THIRD: {}
            
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