import random


class Snake:
    
    def __init__(self) -> None:
        self.body=[[1,2],[1,1]]
        self.map=Map(10)
        self.apple = Apple(self)
        self.turn=0
        self.deadly_eaten=False
        
        
    def draw_snake(self):
        for x,y in enumerate(self.body):
            if x==0:
                self.map.map[y[0]][y[1]]='🧑'
            else:
                self.map.map[y[0]][y[1]]='🍊'
                
                
    def move(self,move:str):
        direction = {'s': (1, 0), 'w': (-1, 0), 'a': (0, -1), 'd': (0, 1)}
        dx,dy=direction[move]
                
       
        
        nexthead = [self.body[0][0] + dx, self.body[0][1] + dy]
        
        if self.check_collided(nexthead):
            return False
        if self.map.map[nexthead[0]][nexthead[1]]=='🍐':
            self.deadly_eaten=True
            return False
        if nexthead in [[x,y] for x,y,_ in self.apple.apple]:
            if nexthead==self.apple.apple[0][:2]:
                self.body.append(self.body[-1])
            elif self.map.map[nexthead[0]][nexthead[1]]=='🍏':
                self.map.map[self.body[-1][0]][self.body[-1][1]] = '⬜'
                if len(self.body) > 2:
                    self.map.map[self.body[-2][0]][self.body[-2][1]] = '⬜'
                    self.body = self.body[:-1]


        else:
            self.map.map[self.body[-1][0]][self.body[-1][1]] = '⬜'
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i-1]
        self.body[0]=nexthead    
        if nexthead in [[x,y] for x,y,_ in self.apple.apple]:
            if nexthead==self.apple.apple[0][:2]:
                self.apple.recreate_apple('red')
            else:
                self.apple.recreate_apple('green')
        self.turn +=1 
        if self.turn%10==0:
            if self.map.map[random.randint(1,8)][random.randint(1,8)]=='⬜':
                self.map.map[random.randint(1,8)][random.randint(1,8)]='🍐'
            
        return True
    
    def check_collided(self,body_part):
        return body_part in self.body or body_part[0] in [0, 9] or body_part[1] in [0, 9]
        
        
class Apple:
    def __init__(self,snake:Snake) -> None:
        self.apple=[[random.randint(2,5),random.randint(1,8),'🍎'],[random.randint(6,8),random.randint(1,8),'🍏']]
        self.snake = snake
        self.score = 0
        
    def draw_apple(self):
        for apple in self.apple:
            self.snake.map.map[apple[0]][apple[1]] = apple[2]
            
    
    def recreate_apple(self,apple_type):
        if apple_type=='red':
            self.apple[0]=[random.randint(1,8),random.randint(1,8),'🍎']
            while not self.snake.map.map[self.apple[0][0]][self.apple[0][1]]=='⬜':
                self.apple[0] = [random.randint(1, 8), random.randint(1, 8), '🍎']
            self.score +=1
        elif apple_type=='green':
            self.apple[1] = [random.randint(1, 8), random.randint(1, 8),'🍏']
            while not self.snake.map.map[self.apple[1][0]][self.apple[1][1]]=='⬜':
                self.apple[1] = [random.randint(1, 8), random.randint(1, 8),]
            

    def print_score(self):
        return self.score
    
                

class Map:
    
    
    def __init__(self,size) -> None:
        self.map= []
        for i in range(size):
            row = []
            for j in range(size):
                if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                    row.append("⬛")
                else:
                    row.append("⬜")
            self.map.append(row)
        
    def draw_map(self):
        rows = [''.join(row) for row in self.map]
        return ('\n'.join(rows))

    
            
