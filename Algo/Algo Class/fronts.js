// Add Front: Write a method that accepts a value and create a new node, assign it to the list head, and return a pointer to the new head node
class SLLNode {
    constructor(value, next=null) {
        this.value = value;
        this.next = next;
    }
}

class SLL {
    constructor(node) {
        this.head = node;
    }

    addfront(value) {
        var newNode = new SLLNode(value,this.head);
        this.head = newNode;
        return this;
    }
    //Remove Front: write a method to remove the head node and return the new list head node. If the list is empty, return null
    removeFront(){
        if (this.head.next) {
            this.head = this.head.next;
        }
        else {
            this.head = null
        }
        return this
    }

    //Front: write a method to return the value (not the node) at the head of the list. if the list is empty return null
    front() {
        if (this.head) { 
            return this.head['value']
        }
        else {
            return null
        }

    }
}