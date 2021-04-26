export class Puzzle {
    name: string;
    description: string;
    words: string[];

    constructor(
        name: string,
        description: string,
        words: string[]
    ) {
        this.name = name;
        this.description = description;
        this.words = [...words];
    }
}
