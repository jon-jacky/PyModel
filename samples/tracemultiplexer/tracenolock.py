"""
tracenolock.py - like tracemultiplexer.py but no synch on tracelock
Simply comment out the check for free tracelock in start_enabled and
finish_enabled.

More details appeear in the tracemultiplexer comment header.
"""

## Parameters

# This simple program has only two threads, with only one API call in each

program = (( 'listfiles', ),  # thread 0
           ( 'openfile', ))   # thread 1

threads = range(len(program))

### State

pc = list() # program counter for each thread
phase = list() # phase of each thread in tracecapture
log = list() # contents of tracelog written by all threads

def reset():
    global pc, phase, log
    pc = [ 0 for thread in program ]
    phase = [ 'ready' for thread in program ]
    log = []

reset()

def accepting():
    return all([ phase[t] == 'exit' for t in threads ])

### Actions

def start_enabled(thread): 
    return (phase[thread] == 'ready')
            # and not [ t for t in threads if phase[t] == 'start']) #lock is free

def start(thread):
    phase[thread] = 'start' # acquire lock
    log.append((thread, program[thread][pc[thread]], 'start')) # write log

def call_enabled(thread):
    return phase[thread] == 'start' # holding lock

def call(thread):
    phase[thread] = 'call' # release lock, execute call

def finish_enabled(thread): 
    return (phase[thread] == 'call')
            # and not [ t for t in threads if phase[t] == 'finish']) #lock is free

def finish(thread):
    phase[thread] = 'finish' # acquire lock
    log.append((thread, program[thread][pc[thread]], 'finish')) # write log

def release_enabled(thread):
    return phase[thread] == 'finish' # holding lock

def release(thread):
    if pc[thread] + 1 < len(program[thread]): # more actions remain
        phase[thread] = 'ready' # release lock
        pc[thread] += 1 # advance to next action
    else:
        phase[thread] = 'exit'  # release lock, indicate done

### Metadata

state = ('pc', 'phase', 'log')

actions = (start, call, finish, release)

enablers = {start:(start_enabled,), call:(call_enabled,),
            finish:(finish_enabled,), release:(release_enabled,)}

domains = { start: { 'thread': threads },
            call: { 'thread': threads },
            finish: { 'thread': threads },
            release: { 'thread': threads }}
