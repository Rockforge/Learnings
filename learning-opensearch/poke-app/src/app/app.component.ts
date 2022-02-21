import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'poke-app';

  pokemon?: any;

  pokemonId: string = '';

  constructor(private http: HttpClient) {}

  getPokemon() {
    this.http.get(`http://localhost:8000/pokemon/${this.pokemonId}`)
      .subscribe(response => {
        this.pokemon = response;
        this.pokemon['image'] = this.pokemon.id
          .toString()
          .padStart(3, 0);
      });
  }
}
