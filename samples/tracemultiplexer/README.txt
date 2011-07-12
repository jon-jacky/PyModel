TraceMultiplexer

This model simulates a multi-threaded program that has been
instrumented to save traces of its API calls in a log.  Instead of
simply calling the API functions, each thread instead calls the
tracecapture function, which calls the API function but also saves the
call (with arguments) and return (with return value) in the trace log.
The tracecapture function uses a lock:

tracelock = lock()

tracecapture(thread_id, call, args): # call is action name
  tracelock.acquire()
  log(thread_id, call, "start", args) # log the call with arguments
  tracelock.release() # release here allows threads to interleave
  ret = call(*args)
  tracelock.acquire()
  log(thread_id, call, "finish", ret) # log the return with return value
  tracelock.release()
  return ret

The purpose of tracelock is to ensure that only one thread at a time
can write to the trace log.  To allow threads to interleave, the first
tracelock.release() *precedes* the call, otherwise the call might
block and hold tracelock, prevent other threads from running while
that call blocks.

When multiple threads are writing the tracelog, there can be
nondeterminism in the order in which API calls and returns are made, and
the order they appear in the trace log.  The purpose of this sample is
to demonstrate that nondeterminism.
