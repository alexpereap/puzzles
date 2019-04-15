class linkedListNode:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

node1 = linkedListNode("3")
node2 = linkedListNode("7")
node3 = linkedListNode("10")

node1.nextNode = node2
node2.nextNode = node3

currentNode = node1 # head

# inser node function
def insertNode(head, valueToInsert):
    currentNode = head
    while currentNode is not None:
        if currentNode.nextNode is None:
            currentNode.nextNode = linkedListNode(valueToInsert)
            return head
        currentNode = currentNode.nextNode

# delete node function
def deleteNode(head, valueToDelete):
    currentNode = head
    previousNode = None
    while currentNode is not None:
        if currentNode.value == valueToDelete:
            if previousNode is None:
                newHead = currentNode.nextNode
                currentNode.nextNode = None
                return newHead # deleted the head
            previousNode.nextNode = currentNode.nextNode
            return head
        previousNode = currentNode
        currentNode = currentNode.nextNode
    return head # value to delete was not found


insertNode(currentNode, '20')
insertNode(currentNode, '30')
insertNode(currentNode, '40')
deleteNode(currentNode, "30")

while currentNode is not None:
    print(currentNode.value)
    currentNode = currentNode.nextNode
