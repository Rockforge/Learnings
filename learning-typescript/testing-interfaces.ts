
interface Checkable {
    check(name: string): boolean;
}

class NameChecker implements Checkable {

    check(name: string): boolean {
        return name.toLowerCase() === 'hello';
    }

}
