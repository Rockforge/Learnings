<?php

// 1. Define a family of algorithms

class LogToFile implements Logger {

    public function log($data)
    {
        var_dump('Log the data to a file');
    }

}

class LogToDatabase implements Logger {

    public function log($data)
    {
        var_dump('Log the data to a database');
    }

}

class LogToXWebService implements Logger {

    public function log($data)
    {
        var_dump('Log the data to a web service');
    }

}


// 2. Encapsulate and make them interchangeable, by making them adhere to a interface

interface Logger {

    public function log($log);
}


class App {

    // Specify that you need to use some kind of logger
    // Doesn't really need to care about the type of logger
    public function log($data, Logger $logger = null)
    {
        $logger = $logger ?? new LogToFile();

        $logger->log($data);
    }

}

$app = new App();

$app->log('Some information', new LogToXWebService());
$app->log('Some information', new LogToDatabase());
$app->log('Some information');
