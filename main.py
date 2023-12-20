import os
for i in range(1, 101):
    if i < 10:
        dir = f'day_0{i}'
        os.makedirs(dir, exist_ok=True)
        with open(f'{dir}/day_0{i}.py', 'w') as f:
            f.write(f'#Its day {i}')
            # os.remove(f'day_0{i}.py')

    else:
        dir = f'day_{i}' 
        os.makedirs(dir, exist_ok=True)
        with open(f'{dir}/day_{i}.py', 'w') as f:
            f.write(f'#Its day {i}')
        # os.remove(f'day_{i}.py')