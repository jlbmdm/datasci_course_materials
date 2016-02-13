import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():

    for line in tweet_file:
        #data.append(json.loads(line))
        lineDict = json.loads(line)
        if lineDict.keys().count(u'text'):
            lineText = lineDict[u'text'].encode('utf8', errors='ignore')
            #print 'Texto1:', lineText
            wordList = lineText.split(" ")
            #print type(wordList)
            #print 'Texto3: ', wordList
            wordListOk = []
            for word in wordList:
                wordOk = word.strip('..').strip('.').strip(':').strip(',').strip(';').strip('?').strip('!').strip('(').strip(')')
                #wordOk = wordOk.strip('"')
                wordListOk.append(wordOk)
            data.append(wordListOk)

    scores = {}
    for line in sent_file:
        term,score = line.split("\t")
        scores[term]=float(score)

    new_terms_sentiment = {}
    new_terms_frecuency = {}
    
    for i in range(len(data)):
        tweet = data[i]
        if len(tweet) > 1 :
            #tweet_word = data[i]["text"].split()
            tweet_word = tweet 
            score = 0
            tweetScores = []
            for word in tweet_word:
                if word in scores.keys():
                    score = score + float(scores[word])
                    tweetScores.append(float(scores[word]))
                else:
                    tweetScores.append(float(0))
            #print score                
            wordNum = 0
            #print tweetScores
            for word in tweet_word:
                #print wordNum 
                if word not in scores.keys():
                    #print "Nuevo", len(tweetScores)
                    n_w_score = float(score)
                    if wordNum == 0:
                        n_w_score += tweetScores[wordNum+1]
                    elif wordNum == len(tweetScores)-1:
                        n_w_score += tweetScores[wordNum-1]
                    else:
                        n_w_score += tweetScores[wordNum+1]+tweetScores[wordNum-1]

                    if word in new_terms_sentiment.keys():
                        new_terms_sentiment[word] = new_terms_sentiment[word] + n_w_score
                        new_terms_frecuency[word] = new_terms_frecuency[word] + 1
                    else:
                        new_terms_sentiment[word] = n_w_score
                        new_terms_frecuency[word] = 1
                wordNum += 1

    for w in new_terms_sentiment:
        new_terms_sentiment[w] = new_terms_sentiment[w] / new_terms_frecuency[w]
        if new_terms_frecuency[w]>0:
            sys.stdout.write(w+' ')
            #print new_terms_frecuency[w]
            print new_terms_sentiment[w]

    
if __name__ == '__main__':
    main()
