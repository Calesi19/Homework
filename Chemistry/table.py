def calculate(slope):
    sum = 0
    for i in range(0, len(slope)):
        print(f'\nTest Tube {i + 1}:')
        print(f'Slope: {slope[i]} * 60 = {slope[i] * 60}')
        sum += slope[i]
    average = sum / 2
    print(f'Average: {average}\n')
    print('########################################')


slope_trial = .01647

slope_one_five = [.01057, .01417]

slope_thirty_two = [ .01060, .01343]

slope_sixty = [ .001865, .003643]

slope_change_one = [ .009207, .01895]

slope_change_two = [ .01427 , .01550]

slope_change_three = [ .002340, .004067]

slopes = {'Test 1.5':slope_one_five, 'Test 32':slope_thirty_two, 'Test 60':slope_sixty, 'Test 1.5-32':slope_change_one, 'Test 32-32':slope_change_two, 'Test 60-32':slope_change_three}

for key in slopes:
    print(f'\n{key}')
    calculate(slopes[key])
