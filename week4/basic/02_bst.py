"""
[이진 검색 트리 - Binary Search Tree (BST)]

문제 설명:
- 이진 검색 트리에서 값을 검색합니다.
- BST 특징: 왼쪽 자식 < 부모 < 오른쪽 자식
- 이 특성을 이용하여 빠른 검색이 가능합니다.
- 왼쪽 서브트리의 모든 값 < 현재 노드 값
- 오른쪽 서브트리의 모든 값 > 현재 노드 값

입력:
- root: 트리의 루트 노드
- target: 찾을 값

출력:
- True: 값이 존재
- False: 값이 없음

예제:
트리:
      5
     / \
    3   7
   / \
  2   4

찾는 값: 4 → True
찾는 값: 6 → False

힌트:
- target < root.value → 왼쪽으로 이동
- target > root.value → 오른쪽으로 이동
- target == root.value → 찾음!

# 이진 검색 트리
왼쪽 서브트리 노드의 키값 < 자신의 노드 키값 + 오른쪽 서브트리 노드의 키값 > 자신의 노드 키값 + 키값이 같은 중복 노드 존재 x
중위순회, 깊이 우선 검색(DFS)으로 검색하면 오름차순 키값을 얻을 수 있다
*깊이 우선 검색 (뿌리->자식으로 최대한 깊숙이 내려갔다가 바로 직전 부모 노드로 돌아와 다시 돌아와 다른길 찾는 방식, 왼쪽 서브트리부터 그 다음 오른쪽. 오른쪽에서도 왼쪽 서브부터 탐색)
*중위 순회: 중간에 부모 노드 방문. 가장 작은 왼쪽 서브까지 - 바로 전 부모 - 가장 큰 오른쪽 서브 순으로 흝기에 오름차순 탐색이 된다
*전위 순회: 부모 - 왼쪽 - 오른쪽
*후위 순회: 왼쪽 - 오른쪽 - 부모
*'위'란 Root의 위치를 뜻한다

# 질문 #
if or elif
inorder?
함수가 돌려주는 값은 bool임 target이 아님
root.value와 root.left의 차이 - 정수와 노드
재귀호출에 인자가 다 없어도 되나? - 안됨
함수 값 돌려주기 주의 출력값은 return 한다
False는 필요없나? - 이미 더 이상 탐색할 노드가 없는 Base case가 False로 설정
먼저 이 함수가 어떤 문제를 해결하는지, I/O이 뭔지 명확하게 하기
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_bst(root, target):
    """
    BST에서 값 검색
    
    Args:
        root: 트리 루트
        target: 찾을 값
    
    Returns:
        True/False
    """
    # TODO: root가 None이면 False 반환
    if root is None: return False
    
    # TODO: 값을 찾으면 True 반환
    ## target이 작으면 왼쪽 서브트리에서 검색
    ## target이 크면 오른쪽 서브트리에서 검색
    if target < root.value:
        return search_bst(root.left, target)
    elif target == root.value:
        return True
    elif target > root.value:
        return search_bst(root.right, target)
        

# 테스트 케이스
if __name__ == "__main__":
    # BST 생성:
    #       5
    #      / \
    #     3   7
    #    / \
    #   2   4
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    
    print("=== 이진 검색 트리 ===")
    print("트리 구조: 5를 루트로 하는 BST")
    
    test_values = [2, 4, 5, 6, 7]
    for val in test_values:
        result = search_bst(root, val)
        print(f"값 {val} 검색: {result}")


