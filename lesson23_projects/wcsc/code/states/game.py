from lesson23_projects.wcsc.auto_gen.data.const import (
    E_GAME_OVER_FLOODGATE,
    E_GAME_OVER_WCSC,
    E_MOVE,
    E_MOVE_ECHO,
)


def create_game(state):
    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        req.context.c_sock.send(f"[WCSC] State path={state_path_str}".encode())

    def __on_trigger(req):
        return req.pull_trigger()

    def __on_move(req):
        pass

    def __on_move_echo(req):
        pass

    def __on_game_over_floodgate(req):
        pass

    def __on_game_over_wcsc(req):
        pass

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    state.on_move = __on_move
    state.on_move_echo = __on_move_echo
    state.on_game_over_floodgate = __on_game_over_floodgate
    state.on_game_over_wcsc = __on_game_over_wcsc
    return state
