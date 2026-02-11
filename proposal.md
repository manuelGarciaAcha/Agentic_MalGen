# Multi-Agent Implementation:

### Basic Idea:
	Update the existing framework to one that implements two agents, as opposed to the basic single-agent configuration. One agent would be the code generator, and the other the code reviewer. This strategy allows for usage of different models for different agents and for improving iterative capabilities.
	
### Implementation:
- Create shared types that the agents and running script can utilize:
	''' Draft{output, assumptions, etc}
	    LoopState{goal, criteria, history[], best_performing}
	    CallGen{goal, constraints, last_review, best_performing}
	    CallRev{Draft, rubric}
	    Result{score, issues[], fixes[], suggestions} '''


	> Runner calls CallGen -> Generator returns Draft -> Runner calls CallRev -> Reviewer returns Result. 
	> Iterations and 'actions' are managed by LoopState


