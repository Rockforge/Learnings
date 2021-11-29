<?php

abstract class HomeChecker {

    protected $successor;

    protected abstract function check(HomeStatus $home);

    // Set the successor for an object
    public function succeedWith(HomeChecker $successor)
    {
        $this->successor = $successor;
    }

    public function next(HomeStatus $home)
    {
        // Check if there is a successor
        if ($this->successor) {
            // Then call this check method
            $this->successor->check($home);
        }
    }
}

class Locks extends HomeChecker {

    public function check(HomeStatus $home)
    {
        if (!$home->locked) {
            throw new Exception('The doors are not locked!! Abort abort.');
        }

        $this->next($home);
    }

}

class Lights extends HomeChecker {

    public function check(HomeStatus $home)
    {
        if (!$home->lightsOff) {
            throw new Exception('The lights are still on!! Abort abort.');
        }

        $this->next($home);
    }

}

class Alarm extends HomeChecker {

    public function check(HomeStatus $home)
    {
        if (!$home->alarmOn) {
            throw new Exception('The alarm has not been set!! Abort abort.');
        }

        $this->next($home);
    }


}

class HomeStatus {

    public $locked = true;
    public $lightsOff = true;
    public $alarmOn = true;

}

// Different ways we can handle the request
// Have the ability to slice through that chain
$locks = new Locks;
$lights = new Lights;
$alarm = new Alarm;

// Creating the chain
$locks->succeedWith($lights);
$lights->succeedWith($alarm);

// Call a check method on the first ring of the chain
$locks->check(new HomeStatus);
