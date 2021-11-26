<?php

interface BookInterface {
    public function open();
    public function turnPage();
}

interface eReaderInterface {
    public function turnOn();
    public function pressNextButton();
}

class Book implements BookInterface {

    public function open()
    {
        var_dump('Opening the paper book');
    }

    public function turnPage()
    {
        var_dump('Turning the page of paper book');
    }
}

class Kindle implements eReaderInterface {

    public function turnOn()
    {
        var_dump('Turn the kindle on');

    }

    public function pressNextButton()
    {
        var_dump('Press the next button on the kindle');
    }

}

class Nook implements eReaderInterface {

    public function turnOn()
    {
        var_dump('Turn the nook on');

    }

    public function pressNextButton()
    {
        var_dump('Press the next button on the nook');
    }

}

class eReaderAdapter implements BookInterface {

    private $eReader;

    public function __construct(eReaderInterface $eReader)
    {
        $this->eReader = $eReader;
    }

    public function open()
    {
        $this->eReader->turnOn();
    }

    public function turnPage()
    {
        $this->eReader->pressNextButton();
    }
}


class Person {

    public function read(BookInterface $book)
    {
        $book->open();
        $book->turnPage();
    }
}

(new Person)->read(new Book);

// Let's adapt our kindle object to be usable by person
// The adapter must adhere to the interface that we wish to implement
$kindle = new eReaderAdapter(new Kindle);

(new Person)->read($kindle);

$nook = new eReaderAdapter(new Nook);

(new Person)->read($nook);
