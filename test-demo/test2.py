# Definition for singly-linked list.
# 给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def add(self, x):
        if self.next is None:
            self.next = ListNode(x)
        else:
            node = self.next
            while node.next:
                node = node.next
            node.next = ListNode(x)
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        arr1 = []
        while l1:
            if l1.val+l2.val<10:
                arr1.append(l1.val+l2.val)
            elif l1.next is None:
                l1.next = ListNode(1)
                arr1.append((l1.val+l2.val) % 10)
            else:
                arr1.append((l1.val + l2.val) % 10)
                l1.next.val += 1
                tmp = l1.next
                while tmp:
                    if tmp.val>=10:
                        if tmp.next is None:
                            tmp.next=ListNode(1)
                            tmp.val=tmp.val%10
                            break
                        else:
                            tmp.next.val += 1
                            tmp.val = tmp.val % 10
                            tmp = tmp.next
                    else:
                        break

            l1 = l1.next
            l2 = l2.next
            if l2 is None:
                break
        if l1 is None and l2 is None:
            pass
        elif l1 is None:
            while l2:
                arr1.append(l2.val)
                l2 = l2.next
        else:
            while l1:
                arr1.append(l1.val)
                l1 = l1.next
        return arr1
if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(8)
    l1.add(9)
    l1.add(9)
    l2 = ListNode(2)
    print(s.addTwoNumbers(l1,l2))