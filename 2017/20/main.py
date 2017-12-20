import re
from collections import defaultdict

def main():

    input_file_name = 'in'

    re_particle_info = r'p=<(.*?)>, v=<(.*?)>, a=<(.*?)>'

    particles = {}

    for i, line in enumerate(open(input_file_name)):
        particle_info = [ list(map(int, x.split(','))) for x in re.findall(re_particle_info, line.rstrip())[0] ]

        particles[i] = particle_info

    for x in range(1000):
        poz = defaultdict(list)
        for p_id, p in particles.items():
            for i in range(3):
                p[1][i] += p[2][i]
                p[0][i] += p[1][i]

        # part 2 start
            poz[tuple(p[0])].append(p_id)

        for position, particle_ids in poz.items():
            if len(particle_ids) > 1:
                for p_id in particle_ids:
                    del particles[p_id]
        # part 2 end

    # closest
    closest_p_value = sys.maxsize
    closest_p = None
    for i, p in particles.items():
        v = sum(map(abs, p[0]))

        if v < closest_p_value:
            closest_p = i
            closest_p_value = v

    print('p1: ', closest_p)
    print('p2: ', len(particles))

if __name__ == '__main__':
    main()
