"""
[이진 트리 - Binary Tree 기본]

문제 설명:
- 이진 트리의 기본 구조를 구현합니다.
- 각 노드는 최대 2개의 자식(왼쪽, 오른쪽)을 가집니다.
- 전위, 중위, 후위 순회를 구현합니다.
- 각 노드가 최대 2개의 자식 노드(왼쪽, 오른쪽)를 가질 수 있는 트리 구조.

입력:
- 트리 노드들

출력:
- 전위 순회: 루트 → 왼쪽 → 오른쪽
- 중위 순회: 왼쪽 → 루트 → 오른쪽
- 후위 순회: 왼쪽 → 오른쪽 → 루트

예제:
트리 구조:
      1
     / \
    2   3
   / \
  4   5

전위: [1, 2, 4, 5, 3]
중위: [4, 2, 5, 1, 3]
후위: [4, 5, 2, 3, 1]

힌트:
- 재귀로 간단히 구현 가능
- 순회 순서만 다름

# 개념 #

# 이진 트리
노드가 왼쪽 자식과 오른쪽 자식만을 갖는 트리. 한 노드당 자식 수는 0~2개까지 전부 가능. 왼쪽과 오른쪽 자식을 구분하며, 각 자식을 루트로 하는 서브트리를 왼쪽 서브트리와 오른쪽 서브트리로 구분한다. 필드(노드 객체가 가진 정보)는 key, value, left, right
*자식은 부모 바로 밑의 한 노드, 서브트리는 그 자식노드를 부모로 삼아 밑 노드까지 포함한 가족 전체

# 완전 이진 트리
마지막 레벨(맨 밑) 제외 모든 모드가 차 있음 + 마지막 레벨에 한해 왼->오로 빈틈없이 노드를 채운다(끝까지 채우지 않아도 o)

# 이진 검색 트리
왼쪽 서브트리 노드의 키값 < 자신의 노드 키값 + 오른쪽 서브트리 노드의 키값 > 자신의 노드 키값 + 키값이 같은 중복 노드 존재 x
중위순회, 깊이 우선 검색(DFS)으로 검색하면 오름차순 키값을 얻을 수 있다
*깊이 우선 검색 (뿌리->자식으로 최대한 깊숙이 내려갔다가 바로 직전 부모 노드로 돌아와 다시 돌아와 다른길 찾는 방식, 왼쪽 서브트리부터 그 다음 오른쪽. 오른쪽에서도 왼쪽 서브부터 탐색)
*중위 순회: 중간에 부모 노드 방문. 가장 작은 왼쪽 서브까지 - 바로 전 부모 - 가장 큰 오른쪽 서브 순으로 흝기에 오름차순 탐색이 된다
*전위 순회: 부모 - 왼쪽 - 오른쪽
*후위 순회: 왼쪽 - 오른쪽 - 부모
*'위'란 Root의 위치를 뜻한다

# 질문 #
순회하는 법: order 함수를 사용한다
루트 값 추가하는 법
순회를 반복하는 법

# 파슨스 질문 #
root.value와 root.left의 결과 차이: 전자는 정수, 후자는 재귀 결과 리스트
postorder preorder: 트리를 리스트로 변환하는 함수. 포스트는 왼쪽 → 오른쪽 → 나, 프리는 나 → 왼쪽 → 오른쪽.
postorder preorder 차이: 전자는 루트를 자식보다 나중에(post) 처리(기록), 후자는 루트를 자식보다 먼저(pre) 처리(기록). 
root.left: 현재 노드의 왼쪽 자식
append 대신 +=를 쓰는 이유: 중첩 리스트가 아니라 리스트 안에 요소들을 넣기 위해(평탄화)
콜스택: 지금 실행하는 함수, 끝난 뒤 돌아갈 곳을 기억하는 메모리 공간
preorder: 나 - 왼쪽 - 오른쪽
inorder: 왼쪽 - 나 - 오른쪽 (이게 중위순회임)
postorder: 왼쪽 오른쪽 나
결국 지금 구현하려는 함수는 인자로 받는 root를 포함한 모든 트리 노드를 정해진 순서대로 순회하는 함수, root는 상대적인 개념

"""

class TreeNode:
    """이진 트리 노드"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    """전위 순회: 루트 → 왼쪽 → 오른쪽"""
    result = []
    
    # TODO: root가 None이면 빈 리스트 반환
    if root is None: return result
    
    # TODO: 루트 값 추가
    result.append(root.value)
    
    # TODO: 왼쪽 서브트리 순회
    result += preorder(root.left)
    
    # TODO: 오른쪽 서브트리 순회
    result += preorder(root.right)
    
    return result

def inorder(root):
    """중위 순회: 왼쪽 → 루트 → 오른쪽"""
    result = []
    
    # TODO: root가 None이면 빈 리스트 반환
    if root is None: return result
    
    # TODO: 왼쪽 서브트리 순회
    result += inorder(root.left)
    
    # TODO: 루트 값 추가
    result.append(root.value)
    
    # TODO: 오른쪽 서브트리 순회
    result += inorder(root.right)
    
    return result

def postorder(root):
    """후위 순회: 왼쪽 → 오른쪽 → 루트"""
    result = []
    
    # TODO: root가 None이면 빈 리스트 반환
    if root is None: return result
    
    # TODO: 왼쪽 서브트리 순회
    result += postorder(root.left)
    
    # TODO: 오른쪽 서브트리 순회
    result += postorder(root.right)
    
    # TODO: 루트 값 추가
    result.append(root.value)
    
    return result

# 테스트 케이스
if __name__ == "__main__":
    # 트리 생성:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("=== 이진 트리 순회 ===")
    print(f"전위 순회: {preorder(root)}")
    print(f"중위 순회: {inorder(root)}")
    print(f"후위 순회: {postorder(root)}")

