#PP15 - Reverse Word Order
def function():
    sentence=str(input('Please Enter a Sentence'))
    sentencesplit=sentence.split()
    sentencereversed=sentencesplit[::-1]
    print(sentencereversed)
function()