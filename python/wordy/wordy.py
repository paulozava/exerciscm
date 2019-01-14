def calculate(question):
    question = question.replace('What is ', ''). \
                        replace('plus plus', '@'). \
                        replace('minus minus', '@'). \
                        replace('plus', '+').\
                        replace('minus', '-').\
                        replace('multiplied by', '*').\
                        replace('divided by', '/').\
                        replace('?', '')
    try:
        return eval(question)
    except:
        raise ValueError('error')