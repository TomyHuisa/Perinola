class Ronda:
    def __init__(self):
        self.jugadores = []

    def __str__(self):
        return "\n".join(str(jugador) for jugador in self.jugadores)

    def agregarJugador(self, jugador):
        if jugador.sinFichas():
            raise ValueError("El jugador no tiene fichas")
        self.jugadores.append(jugador)

    def sacarJugadoresSinFichas(self):
        self.jugadores = [jugador for jugador in self.jugadores if not jugador.sinFichas()]

    def jugadorEnTurno(self):
        return self.jugadores[0]

    def pasarTurno(self):
        if len(self.jugadores) > 1:
            jugador_turno = self.jugadores.pop(0)
            self.jugadores.append(jugador_turno)

    def quedaUnSoloJugador(self):
        return len(self.jugadores) == 1