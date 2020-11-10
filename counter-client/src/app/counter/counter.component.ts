import { Component, OnInit } from '@angular/core';
import { take } from 'rxjs/operators';

import { CounterService } from './counter.service';

@Component({
  selector: 'app-counter',
  templateUrl: './counter.component.html',
  styleUrls: ['./counter.component.scss']
})
export class CounterComponent implements OnInit {
  public count: number;

  constructor(
    private counterService: CounterService
  ) { }

  ngOnInit(): void {
    this.getCount();
  }

  getCount() {
    this.counterService.getCount()
      .pipe(take(1))
      .subscribe(({ value }) => {
        this.count = value;
      });
  }

  decrease() {
    this.counterService.decreaseCount()
      .pipe(take(1))
      .subscribe(({ value }) => {
        this.count = value;
      });
  }
}
