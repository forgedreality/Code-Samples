# Build-a-bot
# 

# Parts:
# arm
# claw
# rocket
# wheel
# gear
# chain

available_parts = [
    'Duster_arm',
    'Speedy_wheel',
    'Grabber_claw',
    'Trashy_rocket',
    'Duster_gear',
    'Duster_chain',
    'Trashy_gear',
    'Speedy_rocket',
    'Trashy_claw',
    'Grabber_claw',
    'Duster_arm',
    'Trashy_chain',
    'Grabber_wheel'
]


def build_dict(parts_list):
    output = {}
    for p in parts_list:
        name, part = p.split('_')

        if name not in output:
            output.update({ name : {part} })
            continue

        output[name].add(part)

    return output


def build_a_bot(reqiuired_parts):
    robots_dict = build_dict(available_parts)
    robots_output = robots_dict.copy()

    buildable_bots = []

    for r in reqiuired_parts:
        for s in robots_dict:
            if r in robots_output[s]:
                robots_output[s].remove(r)
                if len(robots_output[s]) == 0: buildable_bots.append(s)

    return buildable_bots


print(build_a_bot(['arm', 'claw', 'rocket', 'wheel']))