from collections import deque

graph = {}
graph['james'] =['joseph','june','hello']
graph['joseph']=[]
graph['boy']=['joseph']
graph['june'] = ['mxo']
graph['mxo']=[]
graph['hello'] = ['sifiso','mam']
graph['mam'] = []
graph['sifiso'] = ['luke','sam']
graph['sam']=[]
graph['luke'] = ['bam']
graph['bam'] =[]
graph['wam'] =['luke']
graph['jef'] =['sam','wam']


def search(name):
    searchQ = deque()
    searchQ += graph[name]
    searched = []

    while searchQ:
        person = searchQ.popleft()

        if not person in searched:
            if isSeller(person):
                return person + " is a mango seller"
            
            else:
                searchQ += graph[person]
                searched.append(person)
    return "No mango seller in network"
            
def isSeller(name):
    return name[-1]== 'm'

print(search("mxo"))