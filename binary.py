#Sujata Patil
class Node:
     def __init__(self,data):
         self.left = None
         self.right = None
         self.val = data

     def insert(self,value):
          if self.val:
              if value < self.val:
                  if self.left is None:
                      self.left=Node(value)
                  else:
                      self.left.insert(value)
              elif value > self.val:
                  if self.right is None:
                      self.right=Node(value)
                  else:
                      self.right.insert(value)
              else:
                  print("Number already exist")
          else:
              self.val=value

     def PrintTree(self):
            if self.left:
                self.left.PrintTree()
            print(self.val)
            if self.right:
                self.right.PrintTree()

root=0
print("Enter a number")
while(True):
   x= int(input(">"))
   if(x==-1):
       break
   if (root==0):
      root=Node(x)
   else:
       root.insert(x)
if(root==0):
    print("Tree is empty")
else:
    root.PrintTree()
