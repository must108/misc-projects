class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = [root]
        res = []

        while q:
            n = len(q)
            t = []

            for _ in range(n):
                a = q.pop(0)
                t.append(a.val)
                if a.left: q.append(a.left)
                if a.right: q.append(a.right)

            res.append(t)

        return res