<?php

/**
 * Subscriber
 */
interface Observer {
    public function handle();
}

/**
 * Some kind of newsletter/form thread
 * This is also called a Publisher
 */
interface Subject {
    public function attach($observable);
    public function detach($observer);
    public function notify();
    // public function release();
}

class Login implements Subject {

    protected $observers;

    public function attach($observable)
    {
        if (is_array($observable)) {
            return $this->attachObserver($observable);
        }

        $this->observers[] = $observable;

        return $this;
    }

    private function attachObserver($observable)
    {
        foreach ($observable as $observer) {
            if (!$observer instanceof Observer) {
                throw new Exception;
            }
            $this->attach($observer);
        }
        return;
    }

    public function detach($index)
    {
        unset($this->observers[$index]);
    }

    public function notify()
    {
        foreach ($this->observers as $observer) {
            $observer->handle();
        }
    }

    public function fire()
    {
        return $this->notify();
    }
}

class LogHandler implements Observer {

    public function handle()
    {
        var_dump('Log something important');
    }

}

class EmailNotifier implements Observer {

    public function handle()
    {
        var_dump('Fire off an email');
    }

}

class LoginReporter implements Observer {

    public function handle()
    {
        var_dump('do some form of reporting');
    }

}

$login = new Login();

$login->attach([
    new LogHandler,
    new EmailNotifier,
    new LoginReporter
]);

$login->fire();
