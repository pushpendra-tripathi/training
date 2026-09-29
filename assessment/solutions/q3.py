'''
    execution_time module
'''
import time

def execution_time(fn):
    '''
    decorator function for calculating execution time
    '''
    def wrapper_func(*args, **kwargs):
        '''
        wrapper function
        '''
        print(f'starting function {fn.__name__} execution')
        start_time = time.time()
        fn(*args, **kwargs)
        end_time = time.time()
        print('execution time is: ',float(end_time - start_time)*60)
        return end_time - start_time
    return wrapper_func

if __name__ == '__main__':
    @execution_time
    def add():
        '''
        demo function
        '''
        print(1+2)

    add()