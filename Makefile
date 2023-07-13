CXX = g++
CXXFLAGS = -std=c++20 -Wall -MMD -I/opt/homebrew/include
LDFLAGS = -L/opt/homebrew/lib
EXEC = chatmix-controller
OBJECTS = main.o
DEPENDS = ${OBJECTS:.o=.d}

${EXEC}: ${OBJECTS}
	${CXX} ${CXXFLAGS} ${OBJECTS} ${LDFLAGS} -o ${EXEC}

-include ${DEPENDS}

clean:
	rm ${DEPENDS} ${OBJECTS} ${EXEC}