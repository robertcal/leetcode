class UnionFind:
    def __init__(self, n):
        """
        初期化
        n: 要素数
        """
        self.par = [-1] * n  # 親
        self.siz = [1] * n  # 各グループのサイズ

    def root(self, x):
        """
        根を求める
        x: 対象の要素
        return: 根のインデックス
        """
        if self.par[x] == -1:
            return x  # x が根の場合は x を返す
        else:
            self.par[x] = self.root(self.par[x])  # 経路圧縮
            return self.par[x]

    def issame(self, x, y):
        """
        x と y が同じグループに属するかを判定
        x, y: 対象の要素
        return: 同じグループなら True, そうでなければ False
        """
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        """
        x を含むグループと y を含むグループを併合する
        x, y: 対象の要素
        return: 併合が行われた場合は True, すでに同じグループだった場合は False
        """
        # x, y をそれぞれ根まで移動する
        x = self.root(x)
        y = self.root(y)

        # すでに同じグループのときは何もしない
        if x == y:
            return False

        # union by size (y 側のサイズが小さくなるようにする)
        if self.siz[x] < self.siz[y]:
            x, y = y, x

        # y を x の子とする
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    def size(self, x):
        """
        x を含むグループのサイズを取得
        x: 対象の要素
        return: グループのサイズ
        """
        return self.siz[self.root(x)]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {} # email -> index of acc

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.unite(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i

        emailGroup = defaultdict(list) # index of acc -> list of emails
        for e, i in emailToAcc.items():
            leader = uf.root(i)
            emailGroup[leader].append(e)

        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))

        return res
