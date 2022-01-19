'''
길 찾기 게임

- 주어진 입력으로부터 이진트리를 만드는게 핵심이다.
y좌표가 가장 높은 것이 루트이므로 루트부터 맞춰간다.
* Fail/1st/00:57:52/RuntimeError
'''
preorderResult = []
postorderResult = []

class treeNode: ## 노드를 나타내는 클래스. pos는 (x좌표, y좌표)의 튜플이다.
    def __init__(self, pos, value):
        self.left = None
        self.right = None
        self.parent = None
        self.x = pos[0]
        self.y = pos[1]
        self.value = value
    
    # 인자의 node를 조건에 맞게 왼쪽/오른쪽에 삽입.
    # 이미 자식이 있을 경우 더 내려가서 올바른 위치에 삽입한다.
    def setChild(self, node):
        target = self
        
        while True:
            if node.x > target.x: # 자식이 더 클 경우
                if target.right == None: # 오른쪽 자식으로 삽입
                    target.right = node
                    return
                else: # 이미 오른쪽 자식이 있으면 오른쪽 자식으로 내려감
                    target = target.right
                    continue
            
            if node.x < target.x: # 자식이 더 작을 경우
                if target.left == None: # 왼쪽 자식으로 삽입
                    target.left = node
                    return
                else: # 이미 왼쪽 자식이 있으면 왼쪽 자식으로 내려감
                    target = target.left
                    continue
    
    def preorder(self):
        global preorderResult
        preorderResult.append(self.value)
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()
        
    def postorder(self):
        global postorderResult
        if self.left != None:
            self.left.postorder()
        if self.right != None:
            self.right.postorder()
        postorderResult.append(self.value)

def solution(nodeinfo):
    answer = [[]]
    
    tempArr = [] # 각 노드별로 ((x좌표, y좌표), 노드번호)의 튜플이 담김
    for i in range(len(nodeinfo)):
        tempArr.append(((nodeinfo[i][0], nodeinfo[i][1]), i + 1))
        
    # y좌표가 큰 것이 먼저오고, y좌표가 같으면 x좌표가 작은것이 먼저오게 함
    tempArr.sort(key = lambda a : (-a[0][1], a[0][0]))
    
    rootNode = treeNode(tempArr[0][0], tempArr[0][1])
    for i in range(1, len(tempArr)):
        t = treeNode(tempArr[i][0], tempArr[i][1])
        rootNode.setChild(t)
    
    rootNode.preorder()
    rootNode.postorder()
    
    return [preorderResult, postorderResult]